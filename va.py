#First basic step is speech to text
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import time
from time import ctime
import re
import requests
import webbrowser
import bs4
import smtplib #simple mail transfer protocol

#To make sure it listens
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening..")
        audio = r.listen(source,phrase_time_limit=5)
    data = ""
#Exception Handling
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data
#listen()

#Responding
def respond(String):
    print(String)
    tts= gTTS(text=String,lang='en')
    tts.save('speech.mp3')
    playsound.playsound('speech.mp3')
    os.remove('speech.mp3')

#VirtualAssistant actions

def voice_assistant(data):
    """giving your actions"""
    if "how are you" in data:
        listening = True
        respond("Good and doing well")
    if "time" in data:
        listening = True
        respond(ctime())
    if "open google" in data.casefold():
        listening= True
        reg_ex = re.search('open google(.*)',data)
        url = 'https://www.google.com/'
        if reg_ex:
            sub = reg_ex.group(1)
            url = url+'r/'
        webbrowser.open(url)
        respond('Done')
    if "email" in data:
        listening = True
        respond("Whom should i send email to?")
        to = listen()
        edict = {'hello':'mohithchamp@gmail.com','just':'mohithsadhwani@gmail.com'}
        toaddr = edict[to]
        respond("What is the Subject?")
        subject = listen()
        respond("What should i tell that person?")
        message = listen()
        content = 'Subject : {}\n\n{}'.format(subject,message)

        #init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com',587)
        #identify the server
        mail.ehlo()
        mail.starttls()
        #login
        mail.login('mohithchamp@gmail.com','Neversaynever@24') #give your mailid and pwd
        mail.sendmail('mohithchamp@gmail.com',toaddr,content)
        mail.close()
        respond('Email Sent')
        
    if "wiki" in data.casefold():
        listening = True
        respond("What should i Search")
        query = listen()
        response = requests.get('https://en.wikipedia.org/wiki/'+query)
        if response is not None:
            html = bs4.BeautifulSoup(response.text,'html.parser')
            paragraphs = html.select('p')
            intro = [i.text for i in paragraphs]
            halo =' '.join(intro)
        respond(halo[:100])

    if "stop" in data:
        listening = False
        print("Listening Stopped")
        respond("See you Mohith")

    try:
        return listening
    except UnboundLocalError:
        print("Timed Out")
        
#time.sleep(2)
respond("Hey Mohith how are you?") #first greeting
listening = True
while listening == True:
    data = listen()
    listening = voice_assistant(data)
    
    





        
