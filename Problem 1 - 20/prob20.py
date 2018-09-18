factorial  = 1
answer = 0

for n in range (100,0,-1):
    factorial = factorial * n

factorialString = list(str(factorial))

for num in factorialString:
    answer += int(num)

print("Answer : ", answer)
