import re
dataInput = open("../inputs/input_7").read().split("\n")
# dataInput = open("../inputs/sample_input_7").read().split("\n")

handBidPairs = []
for handBidPair in dataInput:
    handBidPairs.append(handBidPair.split())
i = 0    
handsByKind = [[],[],[],[],[],[],[]]
for handBidPair in handBidPairs:
    i += 1
    if re.search(r'([AKQJT98765432]).*?\1.*?\1.*?\1.*?\1', handBidPair[0]):
        handsByKind[6].append(handBidPair)
        print('5', handBidPair)
    elif re.search(r'([AKQJT98765432]).*?\1.*?\1.*?\1', handBidPair[0]):
        handsByKind[5].append(handBidPair)
        print('4', handBidPair)
    elif re.search(r'(?:([AKQJT98765432]).*?\1.*?\1.*?)(?:(?!(?:.*?\1){3}).*?([AKQJT98765432]).*?\2.*?)', handBidPair[0]):
        handsByKind[4].append(handBidPair)
        print('F', handBidPair)
    elif re.search(r'([AKQJT98765432]).*?\1.*?\1', handBidPair[0]):
        handsByKind[3].append(handBidPair)
        print('3', handBidPair)
    elif re.search(r'^(?:(?=.*([AKQJT98765432]).*?\1.*?)(?=.*([AKQJT98765432]).*?\2.*?)(?!\1.*\1)(?!\2.*\2)).*$', handBidPair[0]):
        print('2P', handBidPair)
        handsByKind[2].append(handBidPair)
    elif re.search(r'([AKQJT98765432]).*?\1', handBidPair[0]):
        print('P', handBidPair)
        handsByKind[1].append(handBidPair)
    else:
        print('H', handBidPair)
        handsByKind[0].append(handBidPair)
    if i % 10 == 0:
        input()
print(handsByKind)

custom_order = "23456789TJQKA"
                
scoreList = []
for kind in handsByKind:
    print('kind', kind)
    input()
    scoreList += sorted(kind, key=lambda x: [custom_order.index(c) for c in x[0] if c in custom_order])

print('score list', scoreList)
input()
finalScore = 0
i = 1
for hand in scoreList:
    finalScore += i * int(hand[1])
    i += 1
print(finalScore)

input()
