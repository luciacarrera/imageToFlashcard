import easyocr

def img_to_text(langList):
    reader = easyocr.Reader(langList)
    text = reader.readtext('images/cols2_en.png')
    vocab = []
    for myTuple in text:
        vocab.append(myTuple[1])
    return vocab



img_to_text(['en'])