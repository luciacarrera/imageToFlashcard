from PIL import Image


def image_upload():
    # ask for the name of file
    image_name = input("What is the name of the image you would like to convert? (Don't forget to add .png) ")
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
        while image_check != "yes" and image_check != "no":
            image_check = input("Sorry we did not understand that, please answer with yes or no: ").lower()
        if image_check == "no":
            image_upload()
        if image_check == "yes":
            crop_question = input("Do you want to crop the image? (yes/no) ").lower()
            if crop_question != "yes" and crop_question != "no":
                crop_question = input("Sorry we did not understand that, please answer with yes or no: ").lower()
            if crop_question == "yes":
                image_crop(img)


def image_crop(img):
    print(f"Your image has {img.width} width and {img.height} height. ")
    crop = "yes"
    while crop == "yes":
        # Make sure the answer is positive and number !!!!!!!!!!!!!!!!!!!!!!!!!!
        left = int(input("How many pixels would you like to crop from left? "))
        top = int(input("How many pixels would you like to crop from top? "))
        right = img.width - int(input("How many pixels would you like to crop from right? "))
        bottom = img.height - int(input("How many pixels would you like to crop from bottom? "))

        img_res = img.crop((left, top, right, bottom))
        img_res.show()
        crop = input("Would you like to crop again? (yes/no) ").lower()
        if crop != "yes" and crop != "no":
            crop = input("Sorry we did not understand that, please answer with yes or no: ").lower()


image_upload()
