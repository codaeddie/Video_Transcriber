import subprocess
import os
from openai import OpenAI
import sys
from dotenv import load_dotenv

load_dotenv()  # This loads the variables from .env

def check_ffmpeg():
    try:
        subprocess.run(['ffmpeg', '-version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print("ffmpeg not found. Install it or add it to PATH.")
        sys.exit(1)

def extract_audio(input_file):
    output_file = 'audio.wav'
    subprocess.run(['ffmpeg', '-i', input_file, '-vn', '-acodec', 'pcm_s16le', '-ar', '16000', '-ac', '1', output_file])
    return output_file

def transcribe(audio_file):
    client = OpenAI()  # This will automatically use the API key from the environment
    try:
        with open(audio_file, 'rb') as af:
            transcript = client.audio.transcriptions.create(model="whisper-1", file=af)
        return transcript.text
    except Exception as e:
        print(f"API Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_video_file>")
        sys.exit(1)
    
    check_ffmpeg()
    audio_file = extract_audio(sys.argv[1])
    transcript = transcribe(audio_file)
    print(transcript)