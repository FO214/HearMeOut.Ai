import cohere
import time
import pyttsx3
from speechtowav import record_audio
from wavtotext import wav_to_text

chat_history = [
        {"user_name": "User", "text": "Hey!"},
        {"user_name": "Chatbot", "text": "Hey! How can I help you today?"},
    ]
reader = pyttsx3.init()


def program(history):
    if reader._inLoop:
        reader.endLoop()
    co = cohere.Client(API_KEY)
    reader.setProperty('rate',162)
    
    time.sleep(3) #delay to read the response 
    message  = wav_to_text(record_audio("bomboclat.wav", 3))
    response = co.chat(message=message, chat_history=history)

    answer = response.text

    reader.say(answer)
    reader.runAndWait()
        
    history.append({"user_name": "User", "text": message})
    history.append({"user_name": "Chatbot", "text": answer})
