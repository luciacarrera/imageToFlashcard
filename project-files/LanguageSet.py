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

    # How many language are in the image
    try:
        number_lang = int(input("How many languages do you have in the image? "))
        # only positive numbers
        if number_lang <= 0:
            print("The answer has to be positive number. ")
            csv_file()
        # Create empty list for the language shortcuts
        lang_list = [0]*number_lang
    except ValueError:
        print("The answer has to be numeric.")
        csv_file()
    else:
        return lang_list, langbook


def lang_output(lang_list, langbook):
    try:
        # upload the empty list with languages
        for index in range(len(lang_list)):
            lang = input(f"Write the name of the {index+1} language that appears in the image and hit Enter: ")
            if lang not in langbook:
                print("The language name was not found in the list.")
            else:
                lang_list[index] = (langbook[lang])

    except:
        print("Something went wrong. Try again.")
        lang_output(lang_list, langbook)
    else:
        print(lang_list)


