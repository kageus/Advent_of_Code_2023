import math
dataInput = open("../inputs/input_6").read().split("\n")
# dataInput = open("../inputs/sample_input_6").read().split("\n")

raceTime         = int(dataInput[0][[x.isdigit() for x in dataInput[0]].index(True):].replace(" ", ""))
recordDistance   = int(dataInput[1][[x.isdigit() for x in dataInput[1]].index(True):].replace(" ", ""))
print(f"possible combos {raceTime:,}")
print(f"distance to beat {recordDistance:,}")
print(int((raceTime-math.sqrt(raceTime*raceTime - 4 * recordDistance))/2))
input()

for buttonTime in range(int((raceTime-math.sqrt(raceTime*raceTime - 4 * recordDistance))/2)+1, raceTime-1):
    # speed * time remaining > record time
    # button push time  * (raceTime - button push time) > record time
    print(f"{buttonTime:,}", f"{(buttonTime * (raceTime - buttonTime)):,}", f"{recordDistance:,}")
    input()
    if (buttonTime * (raceTime - buttonTime)) > recordDistance:
        foundLow = buttonTime
        print("low", foundLow)
        break

for buttonTime in range(raceTime - int((raceTime-math.sqrt(raceTime*raceTime - 4 * recordDistance))/2), 1, -1):
    print(f"{buttonTime:,}", f"{(buttonTime * (raceTime - buttonTime)):,}", f"{recordDistance:,}")
    if (buttonTime * (raceTime - buttonTime)) > recordDistance:
        foundHigh = buttonTime +1 
        print("high", foundHigh)
        break

print(f"From {foundHigh} to {foundLow} = {foundHigh - foundLow} combinations")