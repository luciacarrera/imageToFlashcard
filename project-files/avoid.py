def avoid(rc_list, pos):
    toAvoid = ""
    if pos == 0:
        toAvoid = "rows"
    else:
        toAvoid = "cols"
    theList = rc_list[pos]
    SENTENIAL = 700
    print("Please tell us what",toAvoid,"to avoid.\nBe careful,",toAvoid,"start at zero.\nTo stop enter",SENTENIAL)
    num = len(rc_list[pos])
    theNum = 0
    while theNum != SENTENIAL:
        try:
            theNum = int(input("Avoid: "))
        except:
            print("Invalid Response")
            theNum = -1
        else:
            if (theNum >= num and theNum != SENTENIAL ) or theNum < 0:
                print("Couldn't find ",toAvoid," with that number. Try Again")
                theNum = -1
            elif theNum == SENTENIAL:
                print("finishing...")
            else:
                theList[theNum] = 0
    rc_list[pos] = theList
    return rc_list


print(avoid([[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]], 1))
