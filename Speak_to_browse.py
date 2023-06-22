import speech_recognition as sr
import webbrowser
import time ,re

rec = sr.Recognizer()
def record():
    with sr.Microphone() as source:
        print("tell me the name of the website ")
        time.sleep(1)  #here we added a delay of 1 mili sec
        audio=rec.listen(source) #here we store the audio
    
    try:
        comm=rec.recognize_google(audio) #here we decode the audio
        pattern = r'\bopen\s+(\w+)\b'
        match = re.search(pattern, comm)
        if match:
            web_site= match.group(1)
        url = "https://www." + web_site + ".com"  #here we load the website
        webbrowser.open(url)
        
        print("loaded")
    except:
        print("sorry I could not understand ")
    
record()
