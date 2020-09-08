import subprocess as sp
import speech_recognition as sr
import pyttsx3

print(sr.Microphone.list_microphone_names())

print("Welcome to my tools.\n\n")

r=sr.Recognizer()

with sr.Microphone() as source:
    print("start say")
    audio=r.record(source,duration=5)
    print("We got you.. Please wait while we are working on your requirements.")

i=r.recognize_google(audio,language='en-US')

print(i)

if (("check" in i) or ("show" in i) or ("update" in i) or ("is" in i) or ("tell" in i)) and ((("date" in i) and ("today" in i)) or (("today's" in i) and ("date" in i))):
    pyttsx3.speak("Here is today's date.")
    print(sp.getoutput("date"))
else:
    print("We don't support it.")




