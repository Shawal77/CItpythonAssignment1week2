#pyttsx3
#pip install pyttsx3

#failed to compile linux


import pyttsx3

text_speech = pyttsx3.init()

answer = input("What do you want to convert to speech")
text_speech.say(answer)
text_speech.runAndWait()
