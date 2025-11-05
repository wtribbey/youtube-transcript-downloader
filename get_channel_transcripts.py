# fetch_transcripts_resilient.py
import argparse, re, sys, time, subprocess
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import pandas as pd
from tqdm import tqdm

def vid_from_url(url):
    u=urlparse(url); q=parse_qs(u.query)
    if u.netloc.endswith("youtu.be"): return u.path.strip("/")
    if "v" in q and q["v"]: return q["v"][0]
    m=re.search(r"(?:v=|/embed/|/shorts/|youtu\.be/)([A-Za-z0-9_-]{11})", url)
    if m: return m.group(1)
    raise ValueError(f"no video id: {url}")

def safe_name(s, n=120):
    s=re.sub(r"[^\w\s-]","",s); s=re.sub(r"\s+","_",s.strip()); return (s or "untitled")[:n]

def normalize(df):
    lower={c:c.strip().lower() for c in df.columns}
    df=df.rename(columns=lower)
    urlcol=next((c for c in ("url","link","video","video_url") if c in df.columns), df.columns[-1])
    titlecol="title" if "title" in df.columns else None
    datecol="date" if "date" in df.columns else None
    return df,urlcol,titlecol,datecol

def try_yta(video_id, with_ts):
    from youtube_transcript_api import YouTubeTranscriptApi
    chunks = YouTubeTranscriptApi.get_transcript(video_id, languages=['en','en-US','en-GB'])
    lines=[]
    for c in chunks:
        t=c.get("text","").strip()
        if not t: continue
        if with_ts:
            ts=int(c.get("start",0)); mm,ss=divmod(ts,60); lines.append(f"[{mm:02d}:{ss:02d}] {t}")
        else:
            lines.append(t)
    return "\n".join(lines)

def try_ytdlp(url, tmpdir, with_ts, cookies_from_browser=None):
    tmpdir.mkdir(parents=True, exist_ok=True)
    cmd=[sys.executable,"-m","yt_dlp","--skip-download","--write-auto-subs","--write-subs",
         "--sub-lang","en,en-US,en-GB","--sub-format","vtt","-o",str(tmpdir / "%(id)s.%(ext)s"), url,
         "--force-ipv4","--user-agent","Mozilla/5.0"]  # ipv4 helps in some nets
    if cookies_from_browser:
        cmd.extend(["--cookies-from-browser", cookies_from_browser])
    p=subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # parse
    vid=vid_from_url(url)
    vtts=list(tmpdir.glob(f"{vid}*.vtt"))
    if not vtts: raise RuntimeError(f"yt-dlp produced no vtt for {url}\nSTDERR:\n{p.stderr[:4000]}")
    import webvtt
    lines=[]
    for f in vtts:
        for c in webvtt.read(str(f)):
            t=c.text.strip()
            if not t: continue
            if with_ts:
                # rough mm:ss from VTT start "HH:MM:SS.mmm"
                h,m,s=c.start.split(':'); s=int(float(s)); mm=int(m)+int(h)*60
                lines.append(f"[{mm:02d}:{s:02d}] {t}")
            else:
                lines.append(t)
    return "\n".join(lines)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--out", default="transcripts")
    ap.add_argument("--with-timestamps", action="store_true")
    ap.add_argument("--rate-limit", type=float, default=0.4)
    ap.add_argument("--cookies-from-browser", help="chrome | edge | firefox | brave, etc.")
    args=ap.parse_args()

    out=Path(args.out); out.mkdir(parents=True, exist_ok=True)
    tmp=out/"_vtt"; tmp.mkdir(exist_ok=True, parents=True)

    try: df=pd.read_csv(args.csv)
    except Exception: df=pd.read_csv(args.csv, header=None, names=["url"])
    df,urlcol,titlecol,datecol = normalize(df)

    rows=[]; errs=[]
    for i,row in tqdm(df.iterrows(), total=len(df), desc="Transcripts"):
        url=str(row[urlcol]).strip()
        if not url: continue
        try: vid=vid_from_url(url)
        except Exception as e:
            errs.append({"row":i,"url":url,"error":str(e)}); continue
        title=(str(row[titlecol]).strip() if titlecol and pd.notnull(row.get(titlecol)) else "")
        date=(str(row[datecol]).strip() if datecol and pd.notnull(row.get(datecol)) else "")

        fname=f"{i:04d}_{safe_name(title or vid)}.txt"; fpath=out/fname
        try:
            text=None
            # 1) youtube-transcript-api
            try:
                text=try_yta(vid, args.with_timestamps)
                if not text or len(text.strip())<5:
                    raise RuntimeError("empty transcript from API")
            except Exception:
                # 2) yt-dlp fallback (with cookies if provided)
                text=try_ytdlp(url, tmp, args.with_timestamps, cookies_from_browser=args.cookies_from_browser)

            fpath.write_text(
                (f"TITLE: {title or '(unknown)'}\nURL: {url}\nVIDEO_ID: {vid}\n" +
                 (f"DATE: {date}\n" if date else "") +
                 "-"*80 + "\n" + text + "\n"),
                encoding="utf-8"
            )
            rows.append({"index":i,"title":title,"date":date,"url":url,"video_id":vid,
                         "transcript_path":str(fpath),"n_chars":len(text)})

        except Exception as e:
            errs.append({"row":i,"url":url,"video_id":vid,"error":str(e)})

        time.sleep(args.rate_limit)

    pd.DataFrame(rows).to_csv(out/"manifest.csv", index=False)
    if errs: pd.DataFrame(errs).to_csv(out/"errors.csv", index=False)
    print(f"Saved transcripts to: {out.resolve()}")
    if errs: print(f"Completed with {len(errs)} issue(s). See {str((out/'errors.csv').resolve())}")

if __name__ == "__main__":
    main()