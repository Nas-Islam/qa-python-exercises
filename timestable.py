def timestable(number):
    for i in range(1, number+1):
        for j in range(1, number+1):
            mp = i * j
            print(mp, end = "\t")
        print(" ")
                
timestable(13)
