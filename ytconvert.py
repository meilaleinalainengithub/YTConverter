import os
from pytube import YouTube

def download_audio(url):
    print("Downloading audio...")
    yt = YouTube(url=url)
    audio = yt.streams.filter(only_audio=True).first()
    out_file = audio.download()
    base, _ = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)

def download_video(url):
    print("Downloading video...")
    yt = YouTube(url=url)
    video = yt.streams.filter(only_video=True).first()
    out_file = video.download()
    base, _ = os.path.splitext(out_file)
    new_file = base + ".mp4"
    os.rename(out_file, new_file)

print("1. MP3 | 2. MP4")
choose = input()

if choose in ["1", "2"]:
    url = input("URL: ")
    
    if choose == "1":
        download_audio(url)
    elif choose == "2":
        download_video(url)
    
    print("Successfully downloaded!")
else:
    print("Invalid choice. Please enter 1 or 2.")
