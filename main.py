for a in range (1,1000):
    flag = 0
    for x in range (1,1000):
         if (((x % 2 == 0) <= (x % 3 !=0)) or (x + a >= 100)) == 0:
            flag = 1

    if flag == 0:
        print (a)
