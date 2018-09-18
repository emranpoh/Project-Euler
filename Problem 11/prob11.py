arr = []

def calcRight(x,y):
    if(x<17):
        prod = (arr[x][y]*arr[x+1][y]*arr[x+2][y]*arr[x+3][y])
        return prod
    else:
        return 0;

def calcDown(x,y):
    if(y<17):
        prod = (arr[x][y]*arr[x][y+1]*arr[x][y+2]*arr[x][y+3])
        return prod
    else:
        return 0;

def calcDiagUp(x,y):
    if(y>3 and x<17):
        prod = (arr[x][y]*arr[x+1][y-1]*arr[x+2][y-2]*arr[x+3][y-3])
        return prod
    else:
        return 0;

def calcDiagDown(x,y):
    if(x<17 and y<17):
        prod = (arr[x][y]*arr[x+1][y+1]*arr[x+2][y+2]*arr[x+3][y+3])
        return prod
    else:
        return 0;

def main():
    f = open("Problem11\\grid.txt","r")
    inputArray = f.read().splitlines()
    for line in inputArray:
        arr.append(line.split(" "))

    for x in range(0,20):
        for y in range(0,20):
            arr[x][y] = int(arr[x][y])

    print (arr)

    topprod = 0

    for x in range(0,20):
        for y in range(0,20):
            if(arr[x][y] != 0):
                if(calcRight(x,y) > topprod):
                    topprod = calcRight(x,y)
                if(calcDown(x,y) > topprod):
                    topprod = calcDown(x,y)
                if(calcDiagUp(x,y) > topprod):
                    topprod = calcDiagUp(x,y)
                if(calcDiagDown(x,y) > topprod):
                    topprod = calcDiagDown(x,y)
    print(topprod)


main()
