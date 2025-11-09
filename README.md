# Intro Cinematic Template

## Steps

1. Run `download.py`
    1. Set the values for `URL` AND `RESOLUTION`
    2. Select the highest resolution `webm` video and audio streams

2. Fade out and convert the video from `webm` to `mp4`
    - `ffmpeg -i video/video.webm -vf "fade=t=out:st=52:d=2" video/intro_after_splash_screens.mp4`

3. Fade out the audio
    - `ffmpeg -i audio/audio.wav -af "volume=enable='between(t,54,100)':volume=0" -af "afade=t=out:st=52:d=2" audio/audio_final.wav`

4. Convert the video from `webm` to `bk2`
    1. Uncheck Compress Audio
    2. Select the `Bink 1` file format and save the file as `bk2`

5. Convert the audio from `wav` to `wem`
    1. Use Wwise version `2019.2`
    2. In Project Settings, set Default Conversion Settings to Vorbis Quality High
    3. Import the audio file into the Default Work Unit of the Actor-Mixer Hierarchy
    4. Convert the file to `wem`
    5. Retrieve the file from `.cache/Windows/SFX`
    6. Save the `wem` file as `audio/audio.wem`

6. Run `copy_audio.py`

7. Save the `bk2` file as `base/movies/fullscreen/common/intro_after_splash_screens.bk2`

8. Save the `wem` files as `base/sound/soundbanks/media/*.wem`

## Video Commands

### Front trim
```ffmpeg -i video/video.webm -ss 00:00:04 -c:v copy -c:a copy -crf: 0 video/video_front.mp4```

### Back trim
```ffmpeg -i video/video.webm -t 00:00:54 -c:v copy -c:a copy -crf: 0 video/video_back.mp4```

### Fade in
```ffmpeg -i video/video.webm -vf "fade=t=in:st=0:d=5" video/video_fadein.mp4```

### Fade out
```ffmpeg -i video/video.webm -vf "fade=t=out:st=10:d=5" video/video_fadeout.mp4```

## Audio Commands

### Front trim
```ffmpeg -i audio/audio.wav -ss 00:00:04 audio/audio_front.wav```

### Back trim
```ffmpeg -i audio/audio.wav -t 00:00:54 audio/audio_back.wav```

### Mute
```ffmpeg -i audio/audio.wav -af "volume=enable='between(t,54,100)':volume=0" audio/audio_muted.wav```

### Fade in
```ffmpeg -i audio/audio.wav -af "afade=t=in:st=0:d=5" audio/audio_fadein.wav```

### Fade out
```ffmpeg -i audio/audio.wav -af "afade=t=out:st=10:d=5" audio/audio_fadeout.wav```
