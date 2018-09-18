def even(n):
    return int(n/2)

def odd(n):
    return (3*n)+1

def generateSequence(n):
    chainArray = []
    chainArray.append(n)
    while n != 1:
        if ((n % 2) == 0):
            n = even(n)
        else:
            n = odd(n)
        chainArray.append(n)

    return (chainArray)

# MAIN -------------------------------------------------------------------------

highestLen = 0
longestChain = []

for q in range (1,1000000):
    m = generateSequence(q)
    if len(m) > len(longestChain):
        longestChain = m
print("Answer:  ", longestChain[0], " | ", longestChain)
