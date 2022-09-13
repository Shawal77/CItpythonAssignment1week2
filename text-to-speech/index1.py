# using gtts(google text to speech)
# pip install gtts
# now we are ready
from gtts import gTTS
import os
from sys import platform

#fh = open("text.txt",'r')

my_text = "Hello im a text reader"
#my_text = fh.read().splitlines()

language = 'en'

output = gTTS(
    text=my_text,
    lang=language,
    slow=False
)
print(platform)

output.save("output.mp3")
#fh.close()


if platform == "win32":
    #for windows
    os.system("start output.mp3")
elif platform == "linux":
    #linux
    #sudo apt install mpg321
    os.system("mpg321 output.mp3")
elif platform == "darwin":
    #OSX
    pass
