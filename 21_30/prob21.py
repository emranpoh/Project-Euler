def deriveFactors(n):
    factorArray = []
    factorCount = 0
    for i in range(1,n+1):
        if(i in factorArray):
            return factorArray
        if(n%i == 0):
            factorArray.append(i)
            if(int(n/i) not in factorArray):
                if(int(n/i) != n):
                    factorArray.append(int(n/i))
    return factorArray

# MAIN -------------------------------------------------------------------------
initArray = []
mirrorArray = []
count = 0
masterArray = []

for i in range(220,10000):

    initSum = 0
    mirrorSum = 0

    initArray = deriveFactors(i)
    for n in initArray:
        initSum += n
    mirrorArray = deriveFactors(initSum)
    for n in mirrorArray:
        mirrorSum += n
    if(initSum != i):
        if(mirrorSum == i):
            if(i not in masterArray):
                print(i, " | ", initSum, " | ", initArray)
                print("> ", initSum, " | ", mirrorSum, " | ", mirrorArray)
                print()
                masterArray.append(i)
                masterArray.append(initSum)
                count += i
                count += initSum

print(count)
