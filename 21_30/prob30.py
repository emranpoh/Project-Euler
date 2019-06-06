print("Problem 30 : Digit Fifth Powers\n")

for i in range(1000,100000000):

    string = str(i)

    arr = list(string)

    arr = [ int(x) for x in arr ]

    if((arr[0]**4 + arr[1]**4 + arr[2]**4 + arr[3]**4) == i):
        print arr

    # print("Answer : " + arr)
    # print arr
