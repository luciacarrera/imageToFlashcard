# CS 021 Final Project: Image to Flashcards
# Lucía Carrera & Simona Hřebcová 
# Program to convert images to flashcards

def main():
    
    # include welcome text
    welcome()

    # repeat until user wants to stop using program
    repeat = True
    while repeat:

        # give instructions to the user on what they should upload
        instructions()

        # ask user if they want to continue using program
        answer = input("Would you like to make more flashcards?\nPlease answer with yes or no: ")

        # while loop in case they do not answer with yes or no
        while answer != "yes" and answer != "no":
             answer = input("Would you like to make more flashcards?\nPlease answer with yes or no: ")

        # when they answered correctly check if yes or no
        if (answer == "no"):
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
        print(welcomeFile.read())
        
# end of welcome function
       


# function to give instructions to the user on how to properly submit an image
def instructions():
    try:
        instructionsFile = open('instructions.txt',encoding="utf-8")

    # error message in case welcome file missing or corrupt
    except:
        print("Sorry but our instructions have gotten lost")

    # printing of welcome text file
    else:
        print(instructionsFile.read())
        
# end of instructions function



# make main run
main()
