def formatRound(round):
    dicestrings = round.split(",")
    formattedDraw = {"red":0, "green":0, "blue":0} 
    for dicestring in dicestrings:
        matches = ['red', 'green', 'blue']
        for match in matches:
            if (dicestring.find(match) != -1):
                number = ""
                for char in dicestring:
                    if char.isdigit():
                        number += char
                formattedDraw[match]    += int(number)
            continue
        
    return formattedDraw


dataInput = open("../inputs/input_2.txt").read().split("\n")
# dataInput = open("../inputs/sample_input_2.txt").read().split("\n")
gamesList = []
for line in dataInput:
    gamesList.append(str(line))

formattedGames = []


# parse through games and put into managable format
for game in gamesList:
    gameID = game.split(":")[0][5:]
    gameDetails = game.split(":")[1].split(";")
    rounds = []
    for round in gameDetails:
        rounds.append(formatRound(round))
    formattedGames.append((gameID, rounds))
    

# analyze and add valid round ids

totalPower = 0

for game in formattedGames:
    print(game)
    bagHighest = {"red":0, "green":0, "blue":0}
    matches = ['red', 'green', 'blue']
    for round in game[1]:
        for match in matches:
            if round[match] > bagHighest[match]:
                bagHighest[match] = round[match]

    gamePower = bagHighest["red"] * bagHighest["green"] * bagHighest["blue"]
    print(f"{gamePower} * {totalPower} =")
    totalPower += gamePower
    print(f"{totalPower}")

print(f"Final Powers Summed: {totalPower}")