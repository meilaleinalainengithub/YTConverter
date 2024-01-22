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

def download_both(url):
    print("Downloading both...")
    yt = YouTube(url=url)
    both = yt.streams.filter(only_audio=False, only_video=False).first()
    out_file = both.download()
    base, _ = os.path.splitext(out_file)
    new_file = base + ".mp4"
    os.rename(out_file, new_file)

print("1. MP3 | 2. MP4 | 3. BOTH")
choose = input()

if choose in ["1", "2", "3"]:
    url = input("URL: ")
    
    if choose == "1":
        download_audio(url)
    elif choose == "2":
        download_video(url)
    elif choose == "3":
        download_both(url)
    
    print("Successfully downloaded!")
else:
    print("Invalid choice. Please enter 1, 2, or 3.")
