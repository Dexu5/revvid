import os
import shutil
from moviepy.editor import *


def composite_video():

    moviesize = (1280, 720)

    _dir = sorted(os.listdir("dump"))
    audio_clips = [AudioFileClip(f"dump/{x}") for x in _dir if x.startswith("audio")]
    image_clips = [ImageClip(f"dump/{x}") for x in _dir if x.startswith("comment")]

    background = ColorClip(moviesize, color=(26, 26, 27))

    intermission = (
        VideoFileClip("data/transition.mp4").set_duration(0.7).resize(height=720)
    )

    title_img = ImageClip("dump/title.png").set_pos("center").resize(0.7)
    title_audio = AudioFileClip("dump/title.mp3")

    title = (
        CompositeVideoClip([background, title_img], size=moviesize)
        .set_audio(title_audio)
        .set_duration(title_audio.duration)
    )

    final = [title, intermission]

    for audio, image in zip(audio_clips, image_clips):
        clip = (
            CompositeVideoClip(
                [background, image.set_pos("center").resize(0.7)], size=moviesize
            )
            .set_duration(audio.duration)
            .set_audio(audio)
        )
        final.append(clip)
        final.append(intermission)

    end_audio = AudioFileClip('dump/end.mp3')
    final.append(background.set_duration(end_audio.duration).set_audio(end_audio))

    concatenate_videoclips(final).write_videofile(
        "video.mp4", fps=20, codec="libx264", audio_codec="aac"
    )

    shutil.rmtree('dump')


