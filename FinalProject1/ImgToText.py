import pytesseract
from PIL import Image
import easyocr

def img_to_text():
    img = Image.open(r"C:\Users\simona.hrebcova\Desktop\Soukrome\CS_Python\FINAL\FinalProject1\poem.png")
    text = pytesseract.image_to_string(img)
    print(text)


img_to_text()
