from pytubefix import YouTube
from pytubefix.cli import on_progress
from sys import argv
import os
from urllib.error import HTTPError

script_dir = os.path.dirname(os.path.abspath(__file__))
download_path = os.path.join(script_dir, "downloads")

url = argv[1]

try:
    yt = YouTube(url, on_progress_callback = on_progress)
    yd = yt.streams.get_lowest_resolution()
    if yd:
        yd.download(download_path)
        print(f"Downloaded: {yt.title}")
    else:
        print("No stream found with the specified resolution.")
except HTTPError as e:
    print(f"HTTP Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")