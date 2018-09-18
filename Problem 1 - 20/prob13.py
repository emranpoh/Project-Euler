print("Problem 13 : Large Sum")

sum = 0

with open("prob13.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)
        print(int(line))
        sum = sum + int(line)

print("Answer =",sum)
