def isSymbolOnAdjacentSeven(yx, x, y):
    symbols = "@#$%^&*/+-="
    #top
    if y != 0:
        #right
        if x != len(yx[0])-1:
            if yx[y-1][x+1] in symbols:
                return 1
        #mid
        if yx[y-1][x] in symbols:
                return 1
        #left
        if x != 0:
            if yx[y-1][x-1] in symbols:
                return 1
    #mid left
    if x != 0:
        if yx[y][x-1] in symbols:
            return 1
    #bottom
    if y != len(yx)-1:
        #right
        if x != len(yx[0])-1:
            if yx[y+1][x+1] in symbols:
                return 1
        #mid
        if yx[y+1][x] in symbols:
            return 1
        #left
        if x != 0:
            if yx[y+1][x-1] in symbols:
                return 1
    return 0
    

dataInput = open("../inputs/input_3.txt").read().split("\n")
# dataInput = open("../inputs/sample_input_3.txt").read().split("\n")
yx = []

for line in dataInput:
    x = []
    for char in line:
        x.append(char)
    yx.append(x)
print(yx)
isSymbolAdjacent = 0
holdDigits = ""
totalSum = 0
for y in range(0, len(yx)):
    for x in range(0, len(yx[0])):
        if not yx[y][x].isdigit():
            if yx[y][x] not in ".":
                isSymbolAdjacent = 1
            if holdDigits and isSymbolAdjacent:
                totalSum += int(holdDigits)    
            # print(x, y, yx[y][x], 'NOT', isSymbolAdjacent, holdDigits, totalSum)
            # input()
            holdDigits = ""
            isSymbolAdjacent = 0

            continue

        if not isSymbolAdjacent:
            isSymbolAdjacent = isSymbolOnAdjacentSeven(yx, x, y)
        holdDigits += yx[y][x]
        # print(x, y, yx[y][x], '   ', isSymbolAdjacent, holdDigits, totalSum)
        # input()
    # process any adjacent helds before new row
    if holdDigits and isSymbolAdjacent:
        totalSum += int(holdDigits)    
        holdDigits = ""
        isSymbolAdjacent = 0
    # print(x, y, yx[y][x], '   ', isSymbolAdjacent, holdDigits, totalSum, 'end of row')
    # input()
print(totalSum)
