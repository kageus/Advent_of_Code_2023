dataInput = open("../inputs/input_5").read().split("\n\n")
# dataInput = open("../inputs/sample_input_5").read().split("\n\n")

# extract the seed range data
seedDataRaw = list(map(lambda i: int(i), dataInput.pop(0)[7:].split(" ")))
seedRanges = []
for i in range(0, len(seedDataRaw),2):
    seedRanges.append([seedDataRaw[i], seedDataRaw[i+1]])
seedRanges = sorted(seedRanges, key=lambda x: x[0])

print(seedRanges)
input()

# extract the almanac from raw data
almanac = []
for maps in dataInput:
    submaps = maps.split('\n', 1)[1].split("\n")
    mapTypes = []
    for mapRange in submaps:
        mapTypes.append(list(map(lambda i: int(i), mapRange.split(" "))))
    almanac.append(mapTypes)
for i in range(0, len(almanac)):
    almanac[i] = sorted(almanac[i], key=lambda x: x[0])

for potential in range(0, 10000000000):
    print(potential)
    original = potential
    for mapType in reversed(almanac):
        for subrange in mapType:
            if potential in range(subrange[0], subrange[0]+subrange[2]):
                potential = subrange[1] + (potential - subrange[0])
                break
    for seedRange in seedRanges:
        if potential in range(seedRange[0], seedRange[0]+seedRange[1]):
            print(f"lowest found: {original}")
            input()

