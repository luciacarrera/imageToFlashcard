import easyocr

def img_to_text(langList,img):
    reader = easyocr.Reader(['en'])
    text = reader.readtext(img)
    vocab = []
    for myTuple in text:
        vocab.append(myTuple[1])
    return vocab




vocab = img_to_text(['en','ch_sim'],'images/cols3.png')
print(vocab)