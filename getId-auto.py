from googleapiclient.discovery import build
import os
import re

# Your YouTube Data API v3 key
api_key = 'xxx'

# The directory containing your MP3 files
directory = 'audio'

# Use the YouTube Data API to search for videos
youtube = build('youtube', 'v3', developerKey=api_key)

# Regex pattern to match filenames that end with "v=videoID.mp3"
pattern = r'v=.*\.mp3$'

# Iterate over all MP3 files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.mp3') and not filename.endswith('_noads.mp3') and not re.search(pattern, filename):
        # Use the filename (without the extension) as the search string
        search_string = filename[:-4]  # Remove the ".mp3" from the end of the filename

        # Make the API request
        request = youtube.search().list(
            part='snippet',
            maxResults=1,
            q=search_string,
            type='video'
        )
        response = request.execute()

        # If there are no search results, print a message and continue with the next iteration
        if not response['items']:
            print(f"No search results for {search_string}.")
            continue

        # Show the top 3 results to the user
        print(f"\nSearch results for {search_string}:")
        for i, item in enumerate(response['items'], start=1):
            print(f"{i}: {item['snippet']['title']}")

        # Always select the first result
        choice = 1

        # Get the video ID of the chosen video
        video_id = response['items'][choice-1]['id']['videoId']

        # Rename the MP3 file with the video ID
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, filename.replace('.mp3', f'v={video_id}.mp3'))
        os.rename(old_path, new_path)
