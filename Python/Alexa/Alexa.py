#Abdullah Maghraby .. Alexa Project using python

#Libraries
import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser
from datetime import datetime
from datetime import date

def voice_recognition():
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()
    
    # Reading Microphone as source
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjusting for ambient noise for better recognition
        audio = recognizer.listen(source)  # Listening to microphone

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)  # Using Google Speech Recognition to recognize speech
        return text
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
        
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None


def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")
    

def search_words_in_string(words, string):
    words_found = [word for word in words if word in string]
    return len(words_found)
    

def respond(data):
	#Websites
	if search_words_in_string(["Google","google"],data):
		url = "https://www.google.com"
		webbrowser.open(url)
	if search_words_in_string(["Gpt","gpt","Chatgpt","chat gpt","Chat Gpt","Chat","chat"],data):
		url = "https://chatgpt.com"
		webbrowser.open(url)
	
	#Timing
	if search_words_in_string(["Time","time"],data):
		text_to_speech(str(datetime.now().time()))
	if search_words_in_string(["Date","date"],data):
		text_to_speech(str(date.today()))
    

#main process
text_to_speech("Hello Abdullah, How can I help you?")
while 1:
	recognized_text = voice_recognition()
	if recognized_text:
		print(f"You said: {recognized_text}")
		respond(recognized_text)
		#text_to_speech(recognized_text)
