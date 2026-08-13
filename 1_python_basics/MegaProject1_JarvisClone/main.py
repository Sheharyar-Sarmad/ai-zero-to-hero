import sounddevice as sd
import numpy as np
import speech_recognition as sr
import soundfile as sf

# Settings
samplerate = 16000
duration = 5  # seconds

print("Recording... Speak now!")

# Record audio
audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
sd.wait()

# Save to file
sf.write("temp.wav", audio, samplerate)

# Now use SpeechRecognition to read file
recognizer = sr.Recognizer()

with sr.AudioFile("temp.wav") as source:
    audio_data = recognizer.record(source)

text = recognizer.recognize_google(audio_data)
print("You said:", text)