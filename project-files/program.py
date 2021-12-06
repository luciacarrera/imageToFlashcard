# CS 021 Final Project: Image to Flashcards
# Lucía Carrera & Simona Hřebcová 
# Program to convert images to flashcards

# We will be using the Pillow library (Image module)
from PIL import Image as Image
import time

def main():
    
    ## WELCOME
    welcome()

    # repeat until user wants to stop using program
    repeat = True
    while repeat:

        ## INSTRUCTIONS
        # ask user if they want to see the instructions
        answer = input("Would you like to read the instructions?\nPlease answer with yes or no: ").lower()

        # while loop in case they do not answer with yes or no
        while answer != "yes" and answer != "no":
            answer = input("Sorry we did not understand that, please answer with yes or no: ").lower()

        if answer == "yes":
            # give instructions to the user on what they should upload
            instructions()

        ## REPEAT PROGRAM
        # ask user if they want to continue using program
        answer = input("Would you like to make more flashcards?\nPlease answer with yes or no: ").lower()

        # while loop in case they do not answer with yes or no
        while answer != "yes" and answer != "no":
             answer = input("Sorry we did not understand that, please answer with yes or no: ").lower()

        # when they answered correctly check if yes or no
        if answer == "no":
            repeat = False
        
    # end of repeat while loop
    
# end of main function



# function to print out welcome text
def welcome():
    
    # opening of welcome file with try catch
    try:
        welcomeFile = open('welcome.txt',encoding="utf-8")

    # error message in case welcome file missing or corrupt
    except:
        print("Welcome to image to flashcards!")

    # printing of welcome text file
    else:
        line = welcomeFile.readline()
        while line != '':
            print(line, end =" ")
            # slows down program for half a second
            #time.sleep(.5)
            line = welcomeFile.readline()

        # prints out new line
        print()
# end of welcome function
       


# function to give instructions to the user on how to properly submit an image
def instructions():

    # first we will open the written instructions
    try:
        instructionsFile = open('instructions.txt', encoding="utf-8")

    # error message in case welcome file missing or corrupt
    except:
        print("Sorry but our instructions have gotten lost")

    # printing of instruction text file

    else:
        line = instructionsFile.readline()
        while line != '':
            print(line, end=" ")
            # slows down program for half a second
            #time.sleep(1)
            line = instructionsFile.readline()
        # prints out newline
        print()

        answer = input("Would you like to see them?\nPlease answer with yes or no: ").lower()

        while answer != "yes" and answer != "no":
            answer = input("Sorry we did not understand that, please answer with yes or no: ").lower()

        # displaying the image examples
        if answer == "yes":
            print("Loading examples of good images...")
            #time.sleep(3)
            try:
                # examples of good images
                goodImage1 = Image.open("images/good01.webp")
                goodImage2 = Image.open("images/good02.webp")
                badImage1 = Image.open("images/banana.png")

            except:
                print("This is weird, we can't seem to find our examples!")
            else:
                goodImage1.show()
                #time.sleep(1)
                goodImage2.show()

                input("\nReady for the bad examples?\nPress enter to continue")

                # examples of bad images
                badImage1.show()

# end of instructions function



# make main run
main()
