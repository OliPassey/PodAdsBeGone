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
        search_string_space = search_string.replace('-', ' ')  # Replace hyphens with spaces

        # Make the API request
        request = youtube.search().list(
            part='snippet',
            maxResults=3,
            q=search_string,
            type='video'
        )
        response = request.execute()

        # Show the top 3 results to the user
        print(f"\nSearch results for {search_string}:")
        for i, item in enumerate(response['items'], start=1):
            print(f"{i}: {item['snippet']['title']}")

        # Auto-select the best match
        choice = None
        for i, item in enumerate(response['items'], start=1):
            if search_string_space.lower() in item['snippet']['title'].lower().replace('-', ' '):
                choice = i
                break

        # If no match was found, ask the user to select one of the results
        if choice is None:
            choice = int(input(f'Enter the number of your choice for file {filename}: '))

        # Get the video ID of the chosen video
        video_id = response['items'][choice-1]['id']['videoId']

        # Rename the MP3 file with the video ID
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, filename.replace('.mp3', f'v={video_id}.mp3'))
        os.rename(old_path, new_path)
