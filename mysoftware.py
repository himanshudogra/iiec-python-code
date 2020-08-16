import pyttsx3
import os


#pyttsx3.speak("Welcome to my tools.")

print("\nChoose 1: for running chrome browser.")
print("Choose 2: for opening sublime text editor.")
print("Choose 3: for opening Github Desktop.\n")

print("Enter You choice: ",end='')

i=input()

if int(i)== 1:
    os.system("Google\ Chrome")
elif int(i) == 2: 
    os.system("Sublime\ Text")
elif int(i) == 3: 
    os.system("GitHub\ Desktop")
else:
    print("Don't Support.")