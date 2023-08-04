# PodAdsBeGone

I really, really hate advertising. A really simple set of scripts to allow automated removal of adverts from downloaded podcast files.  
The code is not robust, and has been tested / used on approx 1 podcast so far.  

The logic behind the code is  
- Enumerate podcast download directory for files (one podcast per run)
- Search YouTube and add videoIDs to the filenames (Auto and Manual Search / Select available)
- Use SponsorBlock for Ad segments to remove
- Removal

## Requires
YouTube API Key - it is currently quite chatty and will use your quota quite quickly.  

## Installation
- Clone the repo locally  
- Add some files to test with to /audio
- pip install -r
- python <file.py>

## Notes
Code is currently command line only, but I am working on a GUI and making it less individual process based.  
It was tested on the WAN Show podcast and may need some tweaking to work for your content.  
Also goes without saying, this relies on sponsor block having segments for the podcast, and the YouTube version must be identical to the local mp3.  
There is basic error handling should YouTube or SponsorBlock return no data, but it's not clever.
