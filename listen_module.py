import speech_recognition as sr

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    query = ""

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Me: {query}\n")

    except:
        print("Say that again please...")

    return query