import pyttsx3
import os


pyttsx3.speak("Welcome to my tools.")

#print("\n1: launch the chrome browser.")
#print("2: opening sublime text editor.")
#print("3: opening Github Desktop.\n")

#pyttsx3.speak("chat with me with your requirement")
while True:

    print("Chat with me whatever is your requirements: ",end='')

    i=input()

    if ("launch" in i) and ("chrome" in i):
        pyttsx3.speak("Please wait while we are launching Chrome browser."); os.system("Google\ Chrome")
    elif (("run" in i) or ("execute" in i)) and (("github" in i) or ("open" in i)):
        pyttsx3.speak("Please wait while we are opening the Github Desktop for you.");os.system("GitHub\ Desktop")
    elif ("exit" in i) or ("quit" in i):
        break
    else:
        print("don't support.")
