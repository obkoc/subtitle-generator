import whisper
#import os

VIDEO = 'inputs/video.mp4'
MODEL = 'tiny'
#FONT = 'font path'

def extract_audio():
    pass

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
    for i in result['segments']:
        print(f'''Text: {i["text"]},
              Start: {i["start"]},
              End: {i['end']}
              Type: {type(i['end'])}''') # pyright: ignore

def print_subtitles():
    pass

