import whisper
#import os

VIDEO = 'inputs/video.mp4'
MODEL = 'turbo'
#FONT = 'font path'

def transcribe_audio(audio, model):
    model = whisper.load_model(model)
    result = model.transcribe(audio)
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

def print_subtitles():
    pass

