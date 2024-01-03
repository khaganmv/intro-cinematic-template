# Intro Cinematic Template

## Audio

Convert to WEM using Wwise.

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

## Video

Convert to BK2 using RAD Video Tools.

### Front trim
```ffmpeg -i video/video.mp4 -ss 00:00:04 -c:v copy -c:a copy -crf: 0 video/video_front.mp4```

### Back trim
```ffmpeg -i video/video.mp4 -t 00:00:54 -c:v copy -c:a copy -crf: 0 video/video_back.mp4```

### Fade in
```ffmpeg -i video/video.mp4 -vf "fade=t=in:st=0:d=5" -c:v copy -c:a copy -crf: 0 video/video_fadein.mp4```

### Fade out
```ffmpeg -i video/video.mp4 -vf "fade=t=out:st=10:d=5" -c:v copy -c:a copy -crf: 0 video/video_fadeout.mp4```
