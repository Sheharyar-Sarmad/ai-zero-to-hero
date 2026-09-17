import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for i, v in enumerate(voices):
    print(i, v.name)

choice = int(input("Choose voice index: "))
engine.setProperty('voice', voices[choice].id)

print("\nRobo Speaker Ready!")

while True:
    text = input("Enter: ")

    if text.lower() == "exit":
        engine = pyttsx3.init()
        engine.say("Goodbye")
        engine.runAndWait()
        break

    engine = pyttsx3.init()
    engine.setProperty('voice', voices[choice].id)
    engine.say(text)
    engine.runAndWait()
    text = input("Say something (exit to stop): ")

    if text.lower() == "exit":
        engine.say("Goodbye")
        engine.runAndWait()
        break

    engine.say(text)
    engine.runAndWait()
    engine.stop()   # 🔥 THIS is the key fix