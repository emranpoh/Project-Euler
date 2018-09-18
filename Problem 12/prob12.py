def genTriangleNum(n):
    val = 0
    for i in range (0,n+1):
        val+=i
        print(val," | ")
    return val

def deriveFactors(n):
    factorCount = 0
    for i in range(1,n+1):
        if n%i == 0:
            factorCount += 1
    print("Factors : ",factorCount)
    return factorCount



for k in range (0,20):
    genTriangleNum(k)
