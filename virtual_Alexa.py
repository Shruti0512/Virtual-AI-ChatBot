import speech_recognition as sr
import yagmail
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("Hey I am your personal Assistant ")
engine.say("What do you want")
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
# now put the command in try bcoz sometimes microphone does not work

    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source,duration=2)
            voice=listener.listen(source)
            comand= listener.recognize_google(voice,language='en-US')
            comand=comand.lower()
            if 'alexa' in comand:
                comand=comand.replace('alexa','')
                #talk(command)

    except:
        pass
    return comand

def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing '+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M:%S')
        date=datetime.datetime.today().strftime('%Y:%M:%D')
        # for am pm or 24 hours format ('%I:%M %p')
        print(time)
        print(date)
        talk('Current time is '+ time)
        talk('Today date is '+ date)

    elif 'who is' in command:
        person= command.replace('who is','')
        info=wikipedia.summary(person,2)
        talk(info)

    elif 'what is' in command:
        person= command.replace('what is','')
        info=wikipedia.summary(person,1)
        talk(info)
        print(info)

    elif 'date' in command:
        talk('sorry, I have an headache')

    elif 'are you single' in command:
        talk('I am in relationship with WI-FI')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'idiot' in command:
        talk('You are also an idiot')

    elif 'stop' in command:
        talk('Ok')
        exit()
    
    elif 'mail' in command:
        
        
        recognizer=sr.Recognizer()
        with sr.Microphone() as src:
            print('Clearing Background noise:')
            recognizer.adjust_for_ambient_noise(src,duration=5)
            print('waiting for your message:')
            recordedaudio=recognizer.listen(src)
            print('Done Recording:')
        try:
            print('Printing the message: ')
            textt=recognizer.recognize_google(recordedaudio,language='en-US')

            print('Your Message: {}',format(textt))

        except Exception as ex:
                print(ex)
        
        talk('To whom you want to send')
        receiver=str(input())
        message=textt
        
        sender=yagmail.SMTP('chaturvedishruti2001@gmail.com') 
        
        sender.send(to=receiver,subject='This is a virtual alexa automated mails',contents=message)


    else:
        talk('Say it again')
    

while True:
    run_alexa()

## I have yet to add chatterbot if info not found on that basis
## also I have yet to create a database which will store receivers gmail with username if that username is found then send mail to the corresponding gmail.