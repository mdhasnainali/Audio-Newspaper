import requests
from bs4 import BeautifulSoup
import pyttsx3

# working with request & bs4
result = requests.get("https://www.nytimes.com/").text
soup = BeautifulSoup(result, 'lxml')

# create a py-to-text object
speaker = pyttsx3.init()

headlines = soup.find_all('section', class_='story-wrapper')

# Voice rate fixed & set voice type as female voice
newVoiceRate = 130
speaker.setProperty('rate', newVoiceRate)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)

# voice[0] == male voice & voice[1] == female voice

for part in headlines:
    if not part.find('span', class_='e-link-text'):
        print(part.text, '\n')
        speaker.say(part.text)
        speaker.runAndWait()
        speaker.stop()
