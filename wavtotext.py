import speech_recognition as sr

def wav_to_text(filename):
    recognizer = sr.Recognizer()

    text = sr.AudioFile(filename)
    with text as source:
        audio = recognizer.record(source)
    try:
        s = recognizer.recognize_google(audio)
        return s
    except Exception as e:
        print("Exception: "+str(e))