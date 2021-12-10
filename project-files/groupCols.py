def groupCols(rc_list):
    cols = rc_list[1]
    i=0
    sum = 0
    for i in range(0,len(cols)):
        sum += cols[i]
    if(sum < 2):
        print("You must have at least two columns. Sorry but we have to restart the program")
        #main()
    if sum>2:
        print("What columns do you want to have included in the first page of your flashcard?")

    print(sum)

groupCols([[1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1]])