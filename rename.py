import os
import re

# The directory containing your MP3 files
directory = 'audio'

# Iterate over all MP3 files in the directory
for filename in os.listdir(directory):
    if filename.endswith('_noads.mp3'):
        # Extract the title and the date from the filename
        title_date, video_id, _ = filename.rsplit('-', 2)

        # Replace hyphens in the title and date with spaces
        cleaned_title_date = title_date.replace('-', ' ')

        # Construct the new filename
        new_filename = f'{cleaned_title_date} NoAds.mp3'

        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f'Renamed: {filename} -> {new_filename}')
