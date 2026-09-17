import time
import random
import requests
from playsound import playsound

# 🎵 list of alarm sound URLs
sounds = [
    "https://www.soundjay.com/buttons/sounds/beep-01a.mp3",
    "https://www.soundjay.com/buttons/sounds/beep-02.mp3",
    "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3"
]

alarm_time = input("Enter alarm time (HH:MM:SS): ")
print("Alarm set for:", alarm_time)

while True:
    current_time = time.strftime("%H:%M:%S")

    if current_time == alarm_time:
        print("⏰ ALARM!")

        # pick random sound
        url = random.choice(sounds)

        # download sound temporarily
        audio = requests.get(url)
        with open("alarm.mp3", "wb") as f:
            f.write(audio.content)

        # play sound
        playsound("alarm.mp3")
        break

    time.sleep(1)