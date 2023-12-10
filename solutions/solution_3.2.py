def getGearRatio(yx, x, y):
    # print("getting ratio", yx[y][x])
    # input()
    partBuilder = ""
    foundParts = []
    #top
    if y != 0:
        #top left
        if x != 0:
            if yx[y-1][x-1].isdigit():
                partBuilder += yx[y-1][x-1]
                partBuilder = eatLeft(yx, y-1, x-1, partBuilder)
        #top center
        if partBuilder:
            if not yx[y-1][x].isdigit():
                foundParts.append(partBuilder)
                partBuilder = ""
            else:
                partBuilder += yx[y-1][x]
        else:
            if yx[y-1][x].isdigit():
                partBuilder += yx[y-1][x]


        #top right
        if x != len(yx[0])-1:
            if partBuilder:
                if not yx[y-1][x+1].isdigit():
                    foundParts.append(partBuilder)
                    partBuilder = ""
                else:
                    partBuilder += yx[y-1][x+1]
                    partBuilder = eatRight(yx, y-1, x+1, partBuilder)
                    foundParts.append(partBuilder)
                    partBuilder = ""
            else:
                if not yx[y-1][x+1].isdigit():
                    partBuilder = ""
                else:
                    partBuilder += yx[y-1][x+1]
                    partBuilder = eatRight(yx, y-1, x+1, partBuilder)
                    foundParts.append(partBuilder)
                    partBuilder = ""
        if partBuilder:
            foundParts.append(partBuilder)
            partBuilder = ""
        partBuilder = ""
    partBuilder = ""

    #mid left
    if x != 0:
        if yx[y][x-1].isdigit():
            partBuilder += yx[y][x-1]
            partBuilder = eatLeft(yx, y, x-1, partBuilder)
            foundParts.append(partBuilder)
            partBuilder = ""

    #mid right
    if x != len(yx[0])-1:
        if yx[y][x+1].isdigit():
            partBuilder += yx[y][x+1]
            partBuilder = eatRight(yx, y, x+1, partBuilder)
            foundParts.append(partBuilder)
            partBuilder = ""
    

    #bottom
    if y != len(yx)-1:
        #bottom left
        if x != 0:
            if yx[y+1][x-1].isdigit():
                partBuilder += yx[y+1][x-1]
                partBuilder = eatLeft(yx, y+1, x-1, partBuilder)
            else:
                partBuilder = ""
        #bottom center
        if partBuilder:
            if not yx[y+1][x].isdigit():
                foundParts.append(partBuilder)
                partBuilder = ""
            else:
                partBuilder += yx[y+1][x]
        else:
            if yx[y+1][x].isdigit():
                partBuilder += yx[y+1][x]

        #bottom right
        if x != len(yx[0])-1:
            if partBuilder:
                if not yx[y+1][x+1].isdigit():
                    foundParts.append(partBuilder)
                    partBuilder = ""
                else:
                    partBuilder += yx[y+1][x+1]
                    partBuilder = eatRight(yx, y+1, x+1, partBuilder)

                    foundParts.append(partBuilder)
                    partBuilder = ""
            else:
                if not yx[y+1][x+1].isdigit():
                    partBuilder = ""
                else:
                    partBuilder += yx[y+1][x+1]
                    partBuilder = eatRight(yx, y+1, x+1, partBuilder)
                    foundParts.append(partBuilder)
                    partBuilder = ""
        if partBuilder:
            foundParts.append(partBuilder)
            partBuilder = ""
    partBuilder = ""

    # print("foundParts",foundParts)
    if len(foundParts) == 2:
        # print('got a gear with values:', foundParts[0], foundParts[1])
        # input()
        return int(foundParts[0]) * int(foundParts[1])
    
    # print('not a gear')
    # input()
    return 0
    
def eatLeft(yx, y, x, partBuilder):
    # print('eat left', partBuilder)
    if x != 0:
        if yx[y][x-1].isdigit():
            partBuilder = yx[y][x-1] + partBuilder
            partBuilder = eatLeft(yx, y, x-1, partBuilder)
        else:
            return partBuilder
    return partBuilder


def eatRight(yx, y, x, partBuilder):
    # print('eat right', partBuilder)
    if x != len(yx[0])-1:
        if yx[y][x+1].isdigit():
            partBuilder = partBuilder + yx[y][x+1]
            partBuilder = eatRight(yx, y, x+1, partBuilder)
        else:
            return partBuilder
    return partBuilder

dataInput = open("../inputs/input_3").read().split("\n")
# dataInput = open("../inputs/sample_input_3").read().split("\n")
yx = []

for line in dataInput:
    x = []
    for char in line:
        x.append(char)
    yx.append(x)

totalSum = 0
for y in range(0, len(yx)):
    for x in range(0, len(yx[0])):
        if yx[y][x] not in "*":
            # print(x, y, yx[y][x], 'NOT', totalSum)
            continue
        totalSum += getGearRatio(yx, x, y) 
        # print(x, y, yx[y][x], 'GEAR CHECK', totalSum)
    print('end of row:', y+1 )

print(totalSum)