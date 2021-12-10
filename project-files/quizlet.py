def quizlet(rowsCols, vocab):
    rows = rowsCols[0]
    cols = 2
    nRows = len(rows)

    try:
        outfile = open('quizlet.txt', 'w')
    except:
        print("could open text file")
    else:
        numVocab = len(vocab)
        if numVocab < nRows * cols:
            print("Error must restart program")
            #main
        else:
            i = 0
            k = 0
            myStr = ""
            for i in range(0,nRows):
                if rows[i] == 1:
                    myStr = vocab[k] + "\t"+ vocab[k+1]+"\n"
                    outfile.write(myStr)
                k +=2
        outfile.close()

quizlet([[1,0,0,1,1,0],[1,1,1,1]],['hello','w','k','f','h','ss','hello','dddw','hello','wf','wsdfh','dfgw'])
