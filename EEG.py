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

# Function

# Main Function
def menu():
    # Menu Screen
    print("\n\tEmotion-to-Environment Generator") # Title

    print("\n\nMade by: Reece Hannah") # Author

    # Option Screen
    print("\n\tWELCOME TO THE PROGRAM")
    print("\nWhat would you wish to do?")
    print("1)\tDisplay a list of emotions to choose from\n")
    print("2)\tInput what emotion you are feeling\n")
    print("3)\tAdd a new emotion and colour palettte\n")
    print("4)\tDisplay a random emotion & colour palette\n\n")

    # Input Screen
    option = int(input("Enter your choice\n---> "))

    return option

# Main Function
def op1():
    # Menu Screen
    print("\n\tEmotion-to-Environment Generator") # Title

    print("\n\nOption:\nDisplay a list of emotions to choose from") # Option

    f = open("Emotions.txt")
    print("\n" + f.read())

    print("\n\nWhich emotion would you like to choose from?\n")
    choice = str(input("--->")).lower()
# Main Function
def op2():
    # Menu Screen
    print("\n\tEmotion-to-Environment Generator") # Title

    print("\n\nOption:\nnput what emotion you are feeling") # Option

# Main Function
def op3():
    # Menu Screen
    print("\n\tEmotion-to-Environment Generator") # Title

    print("\n\nOption:\nAdd a new emotion and colour palettte") # Option

    # Main Function
def op4():
    # Menu Screen
    print("\n\tEmotion-to-Environment Generator") # Title

    print("\n\nOption:\nDisplay a random emotion & colour palette") # Option

# Global Variables
userChoice = menu()

match userChoice:
    case 1:
        op1()
    case 2:
        op2()
    case 3:
        op3()
    case 4:
        op4()
    case _:
        menu()