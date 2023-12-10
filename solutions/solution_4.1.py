# dataInput = open("../inputs/input_4").read().split("\n")
dataInput = open("../inputs/sample_input_4").read().split("\n")

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
    # print(cardPairs)
    # input()

cardsTotal = 0
for wins, numbers in cardPairs:
    cardTotal = 0
    for win in wins:
        if win in numbers:
            if cardTotal != 0:
                cardTotal *= 2
            else:
                cardTotal = 1
    print(cardTotal)
    cardsTotal += cardTotal

print("Total", cardsTotal)