def rowsCols():
    rows = 0
    while rows == 0:
        try:
            rows = int(input("How many rows are in your image? "))
            if rows < 0:
                rows = int('error')
        except:
            print("invalid response. Try Again")
            rows = 0
        else:
            print(rows)
            rowList = []
            i = 0
            while i > rows:
                rowList[i] = 1
                i += 1
                print(i)
            cols = 0
            while cols <= 0:
                try:
                    cols = int(input("How many columns are in your image? "))
                    if cols < 0:
                        cols = int('error')
                except:
                    print("invalid response. Try Again")
                    cols = 0
                else:
                    colList = []
                    for i in cols:
                        colList[i] = 1
                    rowsCols = (rowList, colList)

                    return rowsCols

print(rowsCols())