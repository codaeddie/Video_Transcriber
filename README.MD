# How to Transcribe Video Using OpenAI's Whisper API: A Guide for the Hopelessly Inept

Are you tired of watching videos like a caveman, struggling to understand what people are saying? Here's how to transcribe your videos using OpenAI's Whisper API, even if you're a bit technotarded.

Prerequisites:
- A Windows machine (no really)
- Basic English comprehension (Must be able to read)

Step 1: Install Python
Open PowerShell as admin and run:

```
winget install Python.Python.3.10
```
Restart PowerShell after this.

Step 2: Set up your project
```
mkdir video_transcriber
cd video_transcriber
python -m venv venv
.\venv\Scripts\Activate.ps1
```
If you already have questions, stop, turn off your pc, and go do something else. 

Step 3: Install required packages
```
pip install openai python-dotenv
```

Step 4: Install ffmpeg
```
winget install Gyan.FFmpeg
```
Restart PowerShell again. Yes, again.

Step 5: Create the script
```
New-Item -Path . -Name "transcribe.py" -ItemType "file"
notepad transcribe.py
```
Paste this into the file:

```python
import subprocess
import os
from openai import OpenAI
import sys
from dotenv import load_dotenv

load_dotenv()

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
    client = OpenAI()
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
```

Step 6: Set up your API key
Create a .env file:

```
New-Item -Path . -Name ".env" -ItemType "file"
notepad .env
```
Add this line to the file:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```
Replace `sk-your-actual-api-key-here` with your real API key. If you don't know how to get an API key, maybe stick to watching videos with the sound on.

Step 7: Run the script
```
python transcribe.py your_video.mp4
```
Replace `your_video.mp4` with the name of your video file. If your video isn't in the same directory, use the full path.

Troubleshooting:
- If Python isn't recognized, you probably screwed up the installation. Go back to step 1.
- If ffmpeg isn't found, add it to your PATH or just give up.
- If you get API errors, double-check your API key. It's probably wrong.

Congratulations! You actually did it. 
