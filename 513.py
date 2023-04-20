for a in range (1,10000):
    flag =0
    for x in range (10,1000000):
        if ((x <= 180 and x >=160) <= ((x %35 == 0) <= (x % a ==0))) == 0:
            flag = 1
            break
    if flag == 0:
        print (a)