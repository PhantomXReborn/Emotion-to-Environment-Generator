'''
Program: Emotion-to-Environment Generator
Author: Reece Hannah
Language: Python
Purpose: 
The goal is to explore how emotions 
shape perception and mood by translating
internal feelings into external, 
imagined spaces.
'''

# Imports
import os
import linecache
import random
from time import sleep

# clear_screen Function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading():
    for i in range(5):
        for j in range(3):
            print(j*"*")
            sleep(0.1)
            clear_screen()

        clear_screen()

# Main Function
def menu():
    # Menu Screen
    print("\n\tEmotion-to-Environment Generator") # Title

    print("\n\nMade by: Reece Hannah") # Author

    # Option Screen
    print("\n\tWELCOME TO THE PROGRAM")
    print("\nWhat would you wish to do?")
    print("1)\tDisplay a list of emotions to choose from\n")
    print("2)\tWhat emotion would you wish to learn about\n")
    print("3)\tDisplay a random emotion & colour palette\n\n")

    # Input Screen
    option = int(input("Enter your choice\n---> "))

    return option

# op1 Function
def op1():
    # Menu Screen
    print("\n\tEmotion-to-Environment Generator") # Title

    print("\n\nOption:\nDisplay a list of emotions to choose from") # Option

    f1 = open("Emotions.txt")
    print("\n" + f1.read())

    print("\n\nWhich emotion would you like to choose?\n")
    choice = str(input("--->")).lower()

    for x in f1:
        if choice == x:
            print(linecache.getline('Palettes.txt', x))

# op2 Function
def op2():
    # Menu Screen
    print("\n\tEmotion-to-Environment Generator") # Title

    print("\n\nOption:\nInput what emotion you are feeling") # Option

    emotion = str(input("\n---> "))

    f1 = open("Descript.txt")

    print("\n\nDescription:\n")
    for x in f1:
        if choice == x:
            for i in range(7):
                print(linecache.getline('Descript.txt', (x*7 + i)))

# Main Function
def op3():
    # Menu Screen
    print("\n\tEmotion-to-Environment Generator") # Title

    print("\n\nOption:\nAdd a new emotion and colour palettte") # Option

    emotion_to_append = atr(input("\nEmotion ---> "))
    print("\n")
    palette_to_append = atr(input("\nPalette---> "))

    f1 = open("Emotions.txt")
    f1.write(emotion_to_append + '\n')
    f1.write(palette_to_append + '\n')

    print("\n" + f1.read())

# Main Function
def newEmotion():
    # Menu Screen
    print("\n\tEmotion-to-Environment Generator") # Title

    print("\n\nOption:\nDisplay a random emotion & colour palette") # Option

    with open("Emotions.txt", 'r') as f:
        lines = len(f.readlines())

    random_number = random.randint(1, lines)
    print(linecache.getline('Emotions.txt', random_number))
    print("\n" + linecache.getline('Palettes.txt', random_number))

# Global Variables
userChoice = menu()

match userChoice:
    case 1:
        loading()
        op1()
    case 2:
        loading()
        op2()
    case 3:
        loading()
        op3()
    case 4:
        loading()
        op4()
    case _:
        loading()
        menu()