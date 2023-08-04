from pydub import AudioSegment
import os
import requests

# The directory containing your MP3 files
directory = 'audio'

# Iterate over all MP3 files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.mp3') and not filename.endswith('_noads.mp3'):
        # Extract the YouTube video ID from the filename
        video_id = filename.rsplit('v=', 1)[-1].replace('.mp3', '')
        print(f'VideoID: {video_id}')

        # Construct the URL for the SponsorBlock API request
        url = f'https://sponsor.ajay.app/api/skipSegments?videoID={video_id}'
        print(f'URL: {url}')
        
        # Make the API request
        response = requests.get(url)

        # If the request was successful, cut out the skip segments
        if response.status_code == 200:
            print(f'Skip segment info for {filename}:')
            skip_segments = response.json()
            print(skip_segments)

            # Load the audio file
            audio = AudioSegment.from_mp3(os.path.join(directory, filename))

            # Initialize a list to hold the pieces of the audio file that we want to keep
            pieces = []

            # Start from the beginning of the audio file
            last_end = 0

            # For each skip segment
            for segment in skip_segments:
                # Get the start and end times of the skip segment
                start_time, end_time = segment['segment']

                # Convert from seconds to milliseconds
                start_time *= 1000
                end_time *= 1000

                # Add the piece of audio before the skip segment to the list of pieces to keep
                pieces.append(audio[last_end:int(start_time)])

                # The next piece will start where this skip segment ends
                last_end = int(end_time)

                # Print progress
                progress = 100 * last_end / len(audio)
                print(f'Progress: {progress:.2f}%')

            # Add the piece of audio after the last skip segment to the list of pieces to keep
            pieces.append(audio[last_end:])

            # Concatenate all the pieces together
            processed_audio = sum(pieces)

            # Save the processed audio file
            processed_filename = filename.replace('.mp3', '_noads.mp3')
            processed_audio.export(os.path.join(directory, processed_filename), format='mp3')
            print(f'Processed: {filename}')

            # Remove the original file
            os.remove(os.path.join(directory, filename))
            print(f'Removed: {filename}')
            
        else:
            print(f'Failed to fetch skip segment info for {filename}')
