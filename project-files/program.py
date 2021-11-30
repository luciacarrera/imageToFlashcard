try:
    welcome = open('welcome.txt',encoding="utf-8")
except:
    print("Welcome to image to flashcards!")
else:
    print(welcome.read())
   
    
