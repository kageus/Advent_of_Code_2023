dataInput = open("../inputs/input_4").read().split("\n")
# dataInput = open("../inputs/sample_input_4").read().split("\n")

cardPairs = []
for line in dataInput:
    cards = line.split(":")[1]
    winningNumbers  = cards.split("|")[0]
    winningNumbers  = winningNumbers.strip(" ").split(" ")
    winningNumbers = [int(i) for i in winningNumbers if i]
    haveNumbers     = cards.split("|")[1]
    haveNumbers     = haveNumbers.strip(" ").split(" ")
    haveNumbers = [int(i) for i in haveNumbers if i]
    cardPairs.append((winningNumbers, haveNumbers))

cardCounts = [1] * len(cardPairs)
print(len(cardCounts))
input()

i = 0
for wins, numbers in cardPairs:
    toIndex = i
    winCount = 0
    for win in wins:
        if win in numbers:
            toIndex += 1
            winCount +=1
    if toIndex > i:
        for x in range(i+1, toIndex+1):
            cardCounts[x] += cardCounts[i]
    i += 1

totalCards = 0
for cards in cardCounts:
    totalCards += cards

print(totalCards)


