import math

def prime_eratosthenes(n):
    prime_list = []
    primes = []
    for i in range(2, n+1):
        if i not in prime_list:
            # print (i)
            primes.append(i)
            for j in range(i*i, n+1, i):
                prime_list.append(j)
    return primes

def factorise(a):

    factors = []

    for i in range (1, a/2):
        if((a%i == 0) and (i not in factors)):
            factors.append(i)
            factors.append(a/i)

    print(factors)
    return factors

def checkPerfection(a):

# if sum of x's total divisors == to x -> return 0 (perfect)
# if sum of x's total divisors < to x -> return -1 (deficient)
# if sum of x's total divisors > to x -> return 1 (abundant)

    factors = []

    for i in range (1, a/2):
        if((a%i == 0) and (i not in factors)):
            factors.append(i)
            if(a/i == a):
                continue
            factors.append(a/i)

    totalVal = 0

    for i in factors:
        totalVal += i

    if totalVal == a:
        return 0
    elif totalVal < a:
        return -1
    elif totalVal > a:
        return 1

def checkPentagonal(input):

    output = (math.sqrt(input*24 + 1) + 1)/6

    if(int(output) == output):
        return True

    return False
