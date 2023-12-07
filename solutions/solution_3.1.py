def isSymbolOnAdjacentSeven(xy, x, y):
    symbols = "@#$%^&*/+-"
    #top
    if y != 0:
        #right
        if x != len(xy[0])-1:
            if xy[y-1][x+1] in symbols:
                return 1
        #mid
        if xy[y-1][x] in symbols:
                return 1
        #left
        if x != 0:
            if xy[y-1][x-1] in symbols:
                return 1
    #mid left
    if x != 0:
        if xy[y][x-1] in symbols:
            return 1
    #bottom
    if y != len(xy)-1:
        #right
        if x != len(xy[0])-1:
            if xy[y+1][x+1] in symbols:
                return 1
        #mid
        if xy[y+1][x] in symbols:
            return 1
        #left
        if x != 0:
            if xy[y+1][x-1] in symbols:
                return 1
    return 0
    

dataInput = open("../inputs/input_3.txt").read().split("\n")
# dataInput = open("../inputs/sample_input_3.txt").read().split("\n")
xy = []

for line in dataInput:
    x = []
    for char in line:
        x.append(char)
    xy.append(x)
print(xy)
isSymbolAdjacent = 0
holdDigits = ""
totalSum = 0
for y in range(0, len(xy)):
    for x in range(0, len(xy[0])):
        if not xy[y][x].isdigit():
            print(x, y, xy[y][x], 'NOT', isSymbolAdjacent, holdDigits, totalSum)
            if xy[y][x] in "@#$%^&*/+-":
                isSymbolAdjacent = 1
            if holdDigits and isSymbolAdjacent:
                totalSum += int(holdDigits)    
            holdDigits = ""
            isSymbolAdjacent = 0

            continue

        if not isSymbolAdjacent:
            isSymbolAdjacent = isSymbolOnAdjacentSeven(xy, x, y)
        holdDigits += xy[y][x]
        print(x, y, xy[y][x], '   ', isSymbolAdjacent, holdDigits, totalSum)
    
    # process any adjacent helds before new row
    if holdDigits and isSymbolAdjacent:
        totalSum += int(holdDigits)    
        holdDigits = ""
        isSymbolAdjacent = 0
    print(x, y, xy[y][x], '   ', isSymbolAdjacent, holdDigits, totalSum, 'end of row')
print(totalSum)
