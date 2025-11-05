# Import the necessary library
from youtube_transcript_api import YouTubeTranscriptApi

# 1. Assign the video ID of the YouTube video you want the transcript for
video_id = 'casiJLqt6As' # Example ID, replace with the one you want

try:
    # 2. Fetch the transcript
    # This returns a list of dictionaries, where each dictionary contains
    # the text, start time, and duration of a segment.
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    # 3. Print each line of the transcript
    print(f"Transcript for video: https://www.youtube.com/watch?v={video_id}\n")
    for segment in transcript:
        # The 'text' key contains the actual transcript line
        print(segment['text'])

except Exception as e:
    # Handle cases where transcripts are disabled or an error occurs
    print(f"An error occurred: {e}")
    print(f"Could not retrieve a transcript for video ID '{video_id}'. This might be because:")
    print("- The video does not exist.")
    print("- The video's owner has disabled transcripts.")
    print("- The video is a live stream and has no transcript available yet.")