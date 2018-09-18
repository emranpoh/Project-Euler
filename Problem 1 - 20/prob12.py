def genTriangleNum(n):
    val = 0
    for i in range (0,n+1):
        val+=i
    return val

def deriveFactors(n):
    factorArray = []
    factorCount = 0
    for i in range(1,n+1):
        if(i in factorArray):
            return factorArray
        if(n%i == 0):
            factorArray.append(i)
            if(int(n/i) not in factorArray):
                factorArray.append(int(n/i))
    return factorArray

# MAIN -------------------------------------------------------------------------
for n in range (1,10000000):
    triangleNumber = genTriangleNum(n)
    factorArray = deriveFactors(triangleNumber)
    if(len(factorArray) > 499):
        print("Index: ",n,"\nTriangle Number: ", triangleNumber, "\nLength: ", len(factorArray), "\nArray: ", factorArray)
        break
