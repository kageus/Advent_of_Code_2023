dataInput = open("../inputs/input_7").read().split("\n")
# dataInput = open("../inputs/sample_input_7").read().split("\n")

def determinHandType(handBidPair):
    handBucket = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for char in handBidPair:
        if char == "A":
            handBucket[0] += 1
        elif char == "K":
            handBucket[1] += 1
        elif char == "Q":
            handBucket[2] += 1
        elif char == "J":
            handBucket[3] += 1
        elif char == "T":
            handBucket[4] += 1
        elif char == "9":
            handBucket[5] += 1
        elif char == "8":
            handBucket[6] += 1
        elif char == "7":
            handBucket[7] += 1
        elif char == "6":
            handBucket[8] += 1
        elif char == "5":
            handBucket[9] += 1
        elif char == "4":
            handBucket[10] += 1
        elif char == "3":
            handBucket[11] += 1
        elif char == "2":
            handBucket[12] += 1

    jokerCount = handBucket.pop(3)
    handBucket[handBucket.index(max(handBucket))] += jokerCount
    handBucket.insert(3, 0)
    
    if handBucket.count(5):
        return 6
    elif handBucket.count(4):
        return 5
    elif handBucket.count(3) and handBucket.count(2):
        return 4
    elif handBucket.count(3):
        return 3
    elif handBucket.count(2) == 2:
        return 2
    elif handBucket.count(2):
        return 1
    else:
        return 0

         

handBidPairs = []
for handBidPair in dataInput:
    handBidPairs.append(handBidPair.split())

# TypeMap = {0:"High Card", 1:"Pair", 2:"Two Pair", 3:"Three of a Kind", 4:"Full House",5:"Four of a Kind",6:"Five of a Kind"}
handsByKind = [[],[],[],[],[],[],[]]
for handBidPair in handBidPairs:
    handsByKind[determinHandType(handBidPair[0])].append(handBidPair)
    # print()
    # print(TypeMap[determinHandType(handBidPair[0])],handBidPair[0])
    # input()

custom_order = "J23456789TQKA"              
scoreList = []
for kind in handsByKind:
    scoreList += sorted(kind, key=lambda x: [custom_order.index(c) for c in x[0] if c in custom_order])

finalScore = 0
i = 1
for hand in scoreList:
    finalScore += i * int(hand[1])
    i += 1
print(finalScore)