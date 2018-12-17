print("Problem 18 : Maximum Path Sum 1\n")

array = []
j = 0

with open("Problem 1 - 20/triangle.txt", "r") as ins:
    for line in ins:
        array.append(line.split())

for i in range(len(array)-1,0,-1):

    while(j!=(len(array[i-1]))):

        initPos = int(array[i-1][j])
        lowerPos = int(array[i][j])
        diagPos = int(array[i][j+1])

        if((initPos + lowerPos) > (initPos + diagPos)):
            array[i-1][j] = initPos + lowerPos
        else:
            array[i-1][j] = initPos + diagPos

        j += 1

    j = 0

print("Answer: ", array[0])
