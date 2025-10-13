import whisper
import os

def transcribe_audio():
    model = whisper.load_model("turbo")
    result = model.transcribe("audio.mp3")
    return result["text"]

def create_subtitles():
    pass

