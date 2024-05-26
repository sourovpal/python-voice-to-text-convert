from gtts import gTTS

import os

text = "Hello, how are you today sourav?"

language = 'en'

tts = gTTS(text=text, lang=language, slow=False)

tts.save("output.mp3")

os.system("start output.mp3")  # On Windows
# os.system("afplay output.mp3")  # On macOS
# os.system("mpg321 output.mp3")  # On Linux
