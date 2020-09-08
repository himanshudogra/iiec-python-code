import subprocess as sp
import speech_recognition as sr
import pyttsx3
import os

#print(sr.Microphone.list_microphone_names())

#pyttsx3.speak("Welcome to my tools.\n")

r=sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Go ahead.. I am listening\n")
        audio=r.record(source,duration=6)
        print("We got you.. Please wait while we are working on your requirements.\n")

    i=r.recognize_google(audio,language='en-US')

    print(i)

    #for checking the today's date
    if (("check" in i) or ("show" in i) or ("update" in i) or ("is" in i) or ("tell" in i)) and ((("date" in i) and ("today" in i)) or ("date" in i) or (("today's" in i) and ("date" in i))):
        pyttsx3.speak("Here is today's date.")
        print(sp.getoutput("date"))
        break
    
    #for fetching the ipaddress of Google web servers
    elif (("tell" in i) or ("show" in i) or ("update" in i) or ("check" in i) or ("verify" in i) or ("what is" in i)) and (("Google IP address" in i) or (("IP" in i) and ("Google" in i)) or (("IP" in i) and ("Google's" in i)) or (("IP address" in i) and ("Google's" in i))):
        pyttsx3.speak("Here are the Google's Ipaddress details") 
        print(sp.getoutput("host www.google.com"))
        break

    #for checking the internet connectivity
    elif (("tell" in i) or ("check" in i) or ("update" in i) or ("verify" in i) or ("access" in i)) and (("internet" in i) or ("net" in i) or (("net" in i) and ("working" in i)) or (("internet" in i) and ("working" in i))):
        pyttsx3.speak("Here is the ping output to confirm about the internet connection.")
        print(sp.getoutput("ping -c 5 www.google.com"))
        break

    
    #for displaying the docker version installed on the system
    elif (("check" in i) or ("show" in i) or ("update" in i) or ("run" in i) or ("tell" in i)) and (("docker version" in i) or ("container engine version" in i) or (("docker" in i) and ("version" in i))):
        pyttsx3.speak("Here is the information about the installed Docker version on your machine.")
        print(sp.getoutput("Docker version"))
        break

    #for launching the chrome browser
    elif (("launch" in i) or ("open" in i) or ("run" in i) or ("start" in i)) and (("Chrome" in i) or ("Google Chrome" in i)):
        pyttsx3.speak("Please wait, while we are launching the Chrome browser for you.") 
        os.system("Google\ Chrome")
        print("chrome has launched successfully.\n")
        break

    #for launching the firefox browser
    elif (("launch" in i) or ("open" in i) or ("run" in i) or ("start" in i)) and (("Firefox" in i) or ("Mozilla Firefox" in i)):
        pyttsx3.speak("Please wait, while we are launching the firefox browser for you.")
        os.system("firefox")
        print("firefox has launched successfully.\n")
        break

    #for starting the github Desktop application
    elif (("run" in i) or ("launch" in i) or ("open" in i)or ("start" in i)) and (("GitHub" in i) or ("GitHub desktop" in i)):
        pyttsx3.speak("Please wait while we are opening the Github Desktop for you.")
        os.system("GitHub\ Desktop")
        print("github has successfully started.\n")
        break
    
    #for starting the bluejeans application
    elif (("open" in i) or ("run" in i) or ("start" in i) or ("launch" in i)) and (("bluejeans" in i) or (("blue" in i) and ("jeans" in i))):
        pyttsx3.speak("Please wait while we are starting the Bluejeans for you.")
        os.system("BlueJeans")
        print("BlueJeans has successfully opened.\n")
        break
    
    #for opening the slack channel
    elif (("open" in i) or ("run" in i) or ("start" in i) or ("launch" in i)) and (("slack" in i) or ("slackchat" in i) or ("chatbox" in i) or ("chat box" in i) or ("slackchannel" in i) or ("chat channel" in i) or ("chat app" in i)):
        pyttsx3.speak("Please wait while we are starting the Slack chat for you.")
        os.system("Slack")
        print("Slack Chatbox has started successfully.\n")
        break

    #for starting the Microsoft PowerPoint
    elif (("open" in i) or ("run" in i) or ("start" in i) or ("launch" in i)) and (("Powerpoint" in i) or ("Microsoft PowerPoint" in i) or ("PPT" in i) or ("presentation" in i)):
        pyttsx3.speak("Please wait while we are launching a powerpoint Presentation for you.")
        os.system("Microsoft\ PowerPoint")
        print("Microsoft PowerPoint has started successfully.\n")
        break

    #for opening the Microsoft Excel
    elif (("open" in i) or ("run" in i) or ("start" in i) or ("launch" in i)) and (("excel" in i) or ("microsoftexcel" in i) or ("excelsheet" in i)):
        pyttsx3.speak("Please wait while we are launching a Excel sheet for you.")
        os.system("Microsoft\ Excel")
        print("Microsoft Excel has started successfully.\n")
        break

    #for starting the Outlook
    elif (("open" in i) or ("run" in i) or ("start" in i) or ("launch" in i)) and (("Outlook" in i) or ("mailbox" in i) or ("email box" in i) or ("Microsoft Outlook" in i)):
        pyttsx3.speak("Please wait while we are opening your mailbox.")
        os.system("Microsoft\ Outlook")
        print("Microsoft Outlook has started successfully.\n")
        break
    
    #for launching the Microsoft Word.
    elif (("open" in i) or ("run" in i) or ("start" in i) or ("launch" in i)) and (("WordPad" in i) or ("Microsoft Word" in i) or ("Word file" in i)):
        pyttsx3.speak("Please wait while we are launching a Word file for you.")
        os.system("Microsoft\ Word")
        print("Microsoft Word has started successfully.\n")
        break

    #for launching the Movie Player
    elif (("open" in i) or ("run" in i) or ("start" in i) or ("launch" in i)) and (("I movie" in i) or ("movie" in i)):
        pyttsx3.speak("Please wait while we are starting the movie player for you.")
        os.system("iMovie")
        print("iMovie has started successfully.\n")
        break

    #Asking for feedback and breaking the while loop
    elif ("exit" in i) or ("quit" in i) or ("shutdown" in i) or ("close" in i) or ("kill" in i) or ("stop" in i):
        pyttsx3.speak("Sure. I hope, I was able to fullfill your requirements.")
        feedback=input("How much will you rate this program out of 5? ")
        pyttsx3.speak("Thank You for your valueable feedback. Visit Again!")
        break
    
    #if the respective program is unavailable in the system.
    else:
        print("We don't support it.")
        break
        




