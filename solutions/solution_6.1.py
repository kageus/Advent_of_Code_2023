dataInput = open("../inputs/input_6").read().split("\n")
# dataInput = open("../inputs/sample_input_6").read().split("\n")

race_times         = [int(n) for n in (dataInput[0][[x.isdigit() for x in dataInput[0]].index(True):].split())]
record_distances   = [ int(n) for n in (dataInput[1][[x.isdigit() for x in dataInput[1]].index(True):].split())]
print(race_times)
print(record_distances)

winsList = []
for i in range(0, len(race_times)):
    wins = 0
    print(race_times[i], record_distances[i])
    for buttonTime in range(1, race_times[i]-1):
        # speed * time remaining > record time
        if (buttonTime * (race_times[i] - buttonTime)) > record_distances[i]:
            wins += 1
    winsList.append(wins)

total = 1
print('winsList',winsList)
for wins in winsList:
    total *= wins

print('total',total)