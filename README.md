# PodAdsBeGone

I really, really hate advertising. A really simple set of scripts to allow automated removal of adverts from downloaded podcast files. The code is not robust, and has been tested / used on approx 1 podcast so far.  Whilst this code removes ad's please remember content is not free to create. Consider a regular donation to any creators you want to keep making content, or use this on content you already support.

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

## Usage
- Get a YouTube API v3 API Key from here: https://console.cloud.google.com/ (Restrict it to your public IP, and the YouTube API v3)  
- Add it to line 6 of the getId-x.py files  
- Add a test file to /audio (it should be named almost identically to the youtube video equivelent)
- python getId-search.py
- python removeAds.py

## Notes
Code is currently command line only, but I am working on a GUI and making it less individual process based.  
It was tested on the WAN Show podcast and may need some tweaking to work for your content.  
Also goes without saying, this relies on sponsor block having segments for the podcast, and the YouTube version must be identical to the local mp3.  
There is basic error handling should YouTube or SponsorBlock return no data, but it's not clever.
Rename.py is a work in progress and probably best not used currently.  
getId-auto should only be used when you have confirmed the matching is working as expected by running getId-search.py first.
