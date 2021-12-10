# CS 021 Final Project: Image to Flashcards
# Lucía Carrera & Simona Hřebcová 
# Program to convert images to flashcards

# We will be using the Pillow library (Image module)
from PIL import Image as Image
import time
import easyocr
import csv


def main():
# LUCIA
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


        ## ASK USER FOR IMAGE
        img = image_upload()
        # SIMONA
        ## ASKS USER WHAT LANGUAGES ARE IN THE IMAGE
        langbook = csv_file()
        lang_list = number_lang()
        langList = lang_output(lang_list, langbook)

        ## READS WORDS FROM IMAGE
        vocabList = img_to_text(langList, img)

        ## ASK USER ROWS/COLS
        rc_list = rowsCols()

        ## CREATE QUIZLET FILE ACCORDING TO IF VERTICAL OR HORIZONTAL AND ROWS COLS
        quizlet()

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


#LUCIA
# function to print out welcome text
def welcome():
    
    # opening of welcome file with try catch
    try:
        welcomeFile = open('welcome.txt' ,encoding="utf-8")

    # error message in case welcome file missing or corrupt
    except:
        print("Welcome to image to flashcards!")

    # printing of welcome text file
    else:
        line = welcomeFile.readline()
        while line != '':
            print(line, end=" ")
            # slows down program for half a second
            #time.sleep(.5)
            line = welcomeFile.readline()

        # prints out new line
        print()
# end of welcome function
       

#LUCIA
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
            # time.sleep(1)
            line = instructionsFile.readline()
        # prints out newline
        print()

        answer = input("Would you like to see them?\nPlease answer with yes or no: ").lower()

        while answer != "yes" and answer != "no":
            answer = input("Sorry we did not understand that, please answer with yes or no: ").lower()

        # displaying the image examples
        if answer == "yes":
            print("Loading examples of good images...")
            # time.sleep(3)
            try:
                # examples of good images
                goodImage1 = Image.open("images/good01.webp")
                goodImage2 = Image.open("images/good02.webp")
                badImage1 = Image.open("images/banana.png")

            except:
                print("This is weird, we can't seem to find our examples!")
            else:
                goodImage1.show()
                # time.sleep(1)
                goodImage2.show()

                input("\nReady for the bad examples?\nPress enter to continue")

                # examples of bad images
                badImage1.show()

# end of instructions function


# SIMONA
# function to let user upload image
def image_upload():
    # ask for the name of file
    image_name = input("What is the name of the image you would like to convert? (add .png and the correct path) ")
    img = ""
    try:
        img = Image.open(image_name)

    # Error message
    except:
        print("Something went wrong. Check the image format and location and try again.")
        image_upload()

    else:
        # Display the image and ask if it's the right one
        img.show()
        image_check = input("Is this the right image? (yes/no) ").lower()
        # time.sleep(1)
        while image_check != "yes" and image_check != "no":
            image_check = input("Sorry we did not understand that, please answer with yes or no: ").lower()
        if image_check == "no":
            image_upload()
        return image_name


# LUCIA
# Function that returns list of words it identifies from the image
# parameters are the language list and the image
def img_to_text(langlist,img):
    vocab = []
    text = ()
    try:
        reader = easyocr.Reader(langlist)
    except:
        print("Our ocr does not seem to be working :(")
    else:
        try:
            text = reader.readtext(img)
        except:
            print("Our ocr can't seem to read your image :( ")
        else:
            for myTuple in text:
                vocab.append(myTuple[1])
    # return created list with vocab
    return vocab
# end of instructions function

# SIMONA
# Languages in image
# use csv
# read the csv file
def csv_file():
    try:
        with open('supportedLanguages.csv', mode='r') as csv_language:
            # read the file and split by delimiter
            csv_reader = csv.reader(csv_language, delimiter=';')
            # create empty dictionary and upload with csv file
            langbook = {}
            for row in csv_reader:
                langbook[row[0]] = row[1]

    except Exception as err:
        print(err)

    else:
        return langbook


# Define the languages that has been used
def number_lang():
    # How many language are in the image
    try:
        number_lang = int(input("How many languages do you have in the image? "))
        # only positive numbers
        if number_lang <= 0:
            print("The answer has to be positive number. ")
            number_lang = int(input("How many languages do you have in the image? "))

    except ValueError:
        print('The answer has to be valid integers.')

    else:
        # Create empty list for the language shortcuts
        lang_list = [0] * number_lang
        return lang_list


# Find the shortcuts of used Languages
def lang_output(lang_list, langbook):
    try:
        # upload the empty list with languages
        for index in range(len(lang_list)):
            lang = input(f"Write the name of the {index+1} language that appears in the image and hit Enter: ")
            while lang not in langbook:
                print(f"The {index+1} language name was not found in the list.")
                offer = input("Do you want to see the language offer? (yes/no) ").lower()
                if offer == 'yes':
                    for key in langbook.keys():
                        print(key)
                lang = input(f"Write the name of the {index+1} language that appears in the image and hit Enter: ")
            else:
                lang_list[index] = (langbook[lang])

    except:
        print("Something went wrong.")

    else:
        print(lang_list)
        return lang_list

# function to figure out how many rows and columns the user has in image
def rowsCols():
    rows = 0
    while rows == 0:
        try:
            rows = int(input("How many rows are in your image? "))
        except:
            print("invalid response. Try Again")
        else:
            cols = 0
            while cols == 0:
                try:
                    cols = int(input("How many columns are in your image? "))
                except:
                    print("invalid response. Try Again")
                else:
                    rowsCols = [rows, cols]
                    return rowsCols

# make main run
main()