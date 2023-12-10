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


dataInput = open("../inputs/input_2").read().split("\n")
# dataInput = open("../inputs/sample_input_2").read().split("\n")
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

gameIdTotal = 0

for game in formattedGames:
    print(game)
    bagTotals = {"red":12, "green":13, "blue":14}
    matches = ['red', 'green', 'blue']
    invalidGame = 0
    for round in game[1]:
        if invalidGame == 1:
            break
        print(round)
        for match in matches:
            if round[match] > bagTotals[match]:
                print(f"invalid round - {round[match]} > {bagTotals[match]}")
                invalidGame = 1
                break

    if invalidGame == 0:
        print(f"valid game id {int(game[0])}")
        gameIdTotal += int(game[0])
    else:
        print("invalid game")
    print(gameIdTotal)
    print()