a = 1
b = 2
c = 3
sum = 0

while(c < 4000000):

    a = b
    b = c
    c = a + b

    if(c%2 == 0):
        sum += c

    if(c > 4000000):
        break

print(sum + 2)
