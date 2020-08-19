#This is for MacOS only as for other OS the system application commands like: chrome, firefox, iMovie may differ.

#importing pyttsx3 module in order to use it's speak function. 
import pyttsx3
#importing os module in order to use it's system function.
import os

#calling the speak function belongs to pyttsx3 module for greeting.
pyttsx3.speak("Welcome to my tools. I am here to help you for your requirements")

#while loop will keep on fullfilling your requirements until you explicitly stop it.
while True:

    #This will print the requirement message
    print("Please provide me your requirements: ",end='')

    #input function will be storing the user input into i variable.
    i=input()


    #for fetching the ipaddress of Google web servers
    if (("tell" in i) or ("show" in i) or ("update" in i) or ("check" in i) or ("verify" in i)) and (("google ipaddress" in i) or (("ip" in i) and ("google" in i)) or (("ip" in i) and ("google's" in i)) or (("ipaddress" in i) and ("google's" in i))):
        pyttsx3.speak("Here are the Google's Ipaddress details") 
        os.system("host www.google.com")
        print()

    #for checking the internet connectivity
    elif (("tell" in i) or ("check" in i) or ("update" in i) or ("verify" in i) or ("access" in i)) and (("internet" in i) or ("net" in i) or (("net" in i) and ("working" in i)) or (("internet" in i) and ("working" in i))):
        pyttsx3.speak("Here is the ping output to confirm about the internet connection.")
        os.system("ping -c 5 www.google.com") 
        print()

    
    #for displaying the docker version installed on the system
    elif (("check" in i) or ("show" in i) or ("update" in i) or ("run" in i) or ("tell" in i)) and (("docker version" in i) or ("container engine version" in i) or (("docker" in i) and ("version" in i))):
        pyttsx3.speak("Here is the information about the installed Docker version on your machine.")
        os.system("Docker version") 
        print()

    #for checking the today's date
    elif (("check" in i) or ("show" in i) or ("update" in i) or ("is" in i) or ("tell" in i)) and ((("date" in i) and ("today" in i)) or (("today's" in i) and ("date" in i))):
        pyttsx3.speak("Here's displaying the today's date")
        os.system("date +%D") 
        print()

    #for launching the chrome browser
    elif (("launch" in i) or ("open" in i) or ("run" in i) or ("start" in i)) and (("chrome" in i) or ("googlechrome" in i)):
        pyttsx3.speak("Please wait, while we are launching the Chrome browser for you.") 
        os.system("Google\ Chrome")
        print("chrome has launched successfully.\n")

    #for launching the firefox browser
    elif (("launch" in i) or ("open" in i) or ("run" in i) or ("start" in i)) and (("firefox" in i) or ("mozillafirefox" in i)):
        pyttsx3.speak("Please wait, while we are launching the firefox browser for you.")
        os.system("firefox")
        print("firefox has launched successfully.\n")

    #for starting the github Desktop application
    elif (("run" in i) or ("launch" in i) or ("open" in i)or ("start" in i)) and (("github" in i) or ("githubdesktop" in i)):
        pyttsx3.speak("Please wait while we are opening the Github Desktop for you.")
        os.system("GitHub\ Desktop")
        print("github has successfully started.\n")
    
    #for starting the bluejeans application
    elif (("open" in i) or ("run" in i) or ("start" in i) or ("launch" in i)) and (("bluejeans" in i) or (("blue" in i) and ("jeans" in i))):
        pyttsx3.speak("Please wait while we are starting the Bluejeans for you.")
        os.system("BlueJeans")
        print("BlueJeans has successfully opened.\n")
    
    #for opening the slack channel
    elif (("open" in i) or ("run" in i) or ("start" in i) or ("launch" in i)) and (("slack" in i) or ("slackchat" in i) or ("chatbox" in i) or ("chat box" in i) or ("slackchannel" in i) or ("chat channel" in i) or ("chat app" in i)):
        pyttsx3.speak("Please wait while we are starting the Slack chat for you.")
        os.system("Slack")
        print("Slack Chatbox has started successfully.\n")

    #for starting the Microsoft PowerPoint
    elif (("open" in i) or ("run" in i) or ("start" in i) or ("launch" in i)) and (("powerpoint" in i) or ("microsoftpowerpoint" in i) or ("ppt" in i) or ("presentation" in i)):
        pyttsx3.speak("Please wait while we are launching a powerpoint Presentation for you.")
        os.system("Microsoft\ PowerPoint")
        print("Microsoft PowerPoint has started successfully.\n")

    #for opening the Microsoft Excel
    elif (("open" in i) or ("run" in i) or ("start" in i) or ("launch" in i)) and (("excel" in i) or ("microsoftexcel" in i) or ("excelsheet" in i)):
        pyttsx3.speak("Please wait while we are launching a Excel sheet for you.")
        os.system("Microsoft\ Excel")
        print("Microsoft Excel has started successfully.\n")

    #for starting the Outlook
    elif (("open" in i) or ("run" in i) or ("start" in i) or ("launch" in i)) and (("outlook" in i) or ("mailbox" in i) or ("emailbox" in i) or ("microsoftoutlook" in i)):
        pyttsx3.speak("Please wait while we are opening your mailbox.")
        os.system("Microsoft\ Outlook")
        print("Microsoft Outlook has started successfully.\n")
    
    #for launching the Microsoft Word.
    elif (("open" in i) or ("run" in i) or ("start" in i) or ("launch" in i)) and (("wordpad" in i) or ("microsoftword" in i) or ("microsoft word" in i) or ("word file" in i)):
        pyttsx3.speak("Please wait while we are launching a Word file for you.")
        os.system("Microsoft\ Word")
        print("Microsoft Word has started successfully.\n")

    #for launching the Movie Player
    elif (("open" in i) or ("run" in i) or ("start" in i) or ("launch" in i)) and (("imovie" in i) or ("movie" in i)):
        pyttsx3.speak("Please wait while we are starting the movie player for you.")
        os.system("iMovie")
        print("iMovie has started successfully.\n")

    #Asking for feedback and breaking the while loop
    elif ("exit" in i) or ("quit" in i) or ("shutdown" in i) or ("close" in i) or ("kill" in i) or ("stop" in i):
        pyttsx3.speak("Sure. I hope, I was able to fullfill your requirements.")
        feedback=input("How much will you rate this program out of 5? ")
        pyttsx3.speak("Thank You for your valueable feedback. Visit Again!")
        break
    
    #if the respective program is unavailable in the system.
    else:
        print("Sorry! I don't have such application in my system.\n")
