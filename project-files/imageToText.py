import easyocr

def img_to_text(langList):
    reader = easyocr.Reader(langList)
    text = reader.readtext('images/cols3.png')
    vocab = []
    for myTuple in text:
        vocab.append(myTuple[1])
    print(vocab)





img_to_text(['en','ch_sim'])