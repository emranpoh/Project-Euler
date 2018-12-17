def read(f):
    with open(f, "r") as ins:
        for line in ins:
            line = line.replace("\"",'')
            array = line.split(",")
    return array

print("Problem 22 : Names Scores\n")

nameSum = 0
indexCounter = 0
nameScore = 0
totalNameScore = 0
array = []

    #read file and store elemetns in array and sort
    array = read("Problem 21 - 30/text.txt")
    array = sorted(array)


for i in array:
    indexCounter += 1
    for c in i:
        nameSum += (ord(c)-64)

    # calculate score of name (c) by multiplying sum of Letters and index of Name
    nameScore = nameSum * indexCounter

    # reset nameSum
    nameSum = 0

    print(i, " | ", indexCounter, " | ", nameScore)

    totalNameScore += nameScore

print("--------------------")
print("Answer : ", totalNameScore)
print("--------------------")
