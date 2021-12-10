# we are using csv, need to import csv library
import csv


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
            lang = input(f"Write the name of the {index+1} language that appears in the image and hit Enter: ").lower()
            first_letter = lang[0].upper()
            lang = first_letter + lang[1:]
            if lang not in langbook:
                print(f"The {index+1} language name was not found in the list.")
            else:
                lang_list[index] = (langbook[lang])

    except:
        print("Something went wrong.")

    else:
        return lang_list


langbook = csv_file()
lang_list = number_lang()
lang_output = lang_output(lang_list, langbook)
print(lang_output)
