for a in range (1,1000):
    flag = 0
    for x in range (1,1000):
         if ((x % a == 0) or ((x >= 50 and x<=70) <= (x % 16 !=0))) == 0:
            flag = 1

    if flag == 0:
        print (a)