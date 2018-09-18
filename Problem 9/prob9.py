for n in range (0,1000):
    for i in range (n,1000):
        for m in range (i,1000):
            if ((n + i + m) == 1000):
                if((n * n) + (i * i) == (m * m)):
                    print ("n-",n)
                    print ("i-",i)
                    print ("m-",m)
