from email.mime import audio
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('\nSay aomething\n')
    audio=r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f'You said : {text}')
    except:
        print("Sorry could not recognise your voice5")
