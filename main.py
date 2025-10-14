import whisper
import subprocess

VIDEO = 'inputs/video.mp4'
MODEL = 'turbo'
#FONT = 'font path'

def transcribe_audio(video, model):
    model = whisper.load_model(model)
    result = model.transcribe(video)
    return result

def format_time(unformatted_time:float):
    ms = int(unformatted_time * 1000)
    h , rem = divmod(ms, 3600000)
    m, rem = divmod(rem, 60000)
    s , ms = divmod(rem, 1000)
    return(f'{h:02}:{m:02}:{s:02},{ms:03}')

def create_subtitles(result):
    segments = result['segments']
    with open("output.srt", "w", encoding="utf-8") as f:
        for n, seg in enumerate(segments, start=1):
            f.write(f'{n}\n')
            f.write(f'{format_time(seg["start"])} --> {format_time(seg["end"])}\n')
            f.write(f'{seg["text"]}\n\n')

def print_subtitles(input_file:str, output_file:str, subtitle_file:str):
    cmd = [
    "ffmpeg", "-y",
    "-i", input_file,
    "-vf", f"subtitles={subtitle_file}",
    "-c:v", "libx264", "-crf", "18", "-preset", "medium",
    "-c:a", "copy",
    output_file,
    ]
    subprocess.run(cmd, check=True)

transcribed_audio = transcribe_audio(video=VIDEO, model=MODEL)
subtitles = create_subtitles(result=transcribed_audio)
print_subtitles(input_file=VIDEO, output_file="out.mp4", subtitle_file="output.srt")


