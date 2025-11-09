from pytubefix import YouTube
import subprocess
import os


URL = "https://www.youtube.com/watch?v=rd9mFAZl_SQ"
RESOLUTION = "1440p"

VIDEO_DIR = "video/"
AUDIO_DIR = "audio/"


def init_dirs():
    if not os.path.exists(VIDEO_DIR):
        os.mkdir(VIDEO_DIR)
    
    if not os.path.exists(AUDIO_DIR):
        os.mkdir(AUDIO_DIR)
        

def enumerate_streams(streams, title):
    print(f"Pick an {title} stream:")
    
    for i, stream in enumerate(streams):
        print(f"{i + 1}. {stream}")


def get_stream_index(streams):
    while True:
        index = input("")
        
        if not index.isnumeric():
            print(f"[ error ] invalid index: {index}")
            continue

        index = int(index)

        if index < 1 or index > len(streams):
            print(f"[ error ] index out of bounds: {index}")
            continue
        
        return index - 1


def get_video(video_streams):
    enumerate_streams(video_streams, "video")
    
    video_stream_index = get_stream_index(video_streams)
    
    video_streams[video_stream_index].download(output_path=VIDEO_DIR, filename="video.webm")


def get_audio(audio_streams):
    enumerate_streams(audio_streams, "audio")
    
    audio_stream_index = get_stream_index(audio_streams)
    audio_mime_type = audio_streams[audio_stream_index].mime_type.split("/")[1]
    audio_filename = f"audio.{audio_mime_type}"
    
    audio_streams[audio_stream_index].download(output_path=AUDIO_DIR, filename=audio_filename)
    to_wav(audio_filename)


def to_wav(filename):
    subprocess.call(
        f"ffmpeg -y -i {AUDIO_DIR}{filename} {AUDIO_DIR}audio.wav", 
        shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
    )
    os.remove(f"{AUDIO_DIR}{filename}")


try:
    yt = YouTube(
        URL, 
        use_oauth=True,
        allow_oauth_cache=True
    )
    
    init_dirs()
    get_video(yt.streams.filter(resolution=RESOLUTION))
    get_audio(yt.streams.filter(only_audio=True))
except Exception as e:
    print(e)
