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
    time_ms = int(unformatted_time * 1000)
    hours , remainder = divmod(time_ms, 3600000)
    minutes, remainder = divmod(remainder, 60000)
    seconds , miliseconds = divmod(remainder, 1000)
    return(f'{hours:02}:{minutes:02}:{seconds:02},{miliseconds:03}')

def create_subtitles(result):
    for i in result['segments']:
        print(f'''Text: {i["text"]},
              Start: {i["start"]},
              End: {i['end']}
              Type: {type(i['end'])}''') # pyright: ignore

def print_subtitles():
    pass

