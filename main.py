import whisper
import os

AUDIO = 'audio path'
VIDEO = 'video path'
MODEL = 'small'
FONT = 'font path'

#TODO 
# Try to get .srt from the transcription
# Find a way to get extract audio from video
# Find a way to print subtitles into the video (optional)

def extract_audio():
    pass

def transcribe_audio(audio, model):
    model = whisper.load_model(model)
    result = model.transcribe(audio)
    return result["text"]

def create_subtitles():
    pass

def print_subtitles():
    pass


