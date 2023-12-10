mapKey = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
dataInput = open("../inputs/input_5").read().split("\n\n")
# dataInput = open("../inputs/sample_input_5").read().split("\n\n")
seeds = list(map(lambda i: int(i), dataInput.pop(0)[7:].split(" ")))

almanac = []
for maps in dataInput:
    submaps = maps.split('\n', 1)[1].split("\n")
    mapTypes = []
    for mapRange in submaps:
        mapTypes.append(list(map(lambda i: int(i), mapRange.split(" "))))
    almanac.append(mapTypes)

lowestConversion = float('inf')
for seed in seeds:
    conversion = seed
    i = 0
    for mapTypes in almanac:
        print("Map Type:", mapKey[i], mapTypes)
        for submap in mapTypes:
            # print(submap)
            if conversion in range(submap[1], submap[1]+submap[2]):
                # print(conversion, "in range:", submap[1], "to", submap[1]+submap[2])
                conversion = submap[0]+ (conversion - submap[1])
                # print("after conversion", conversion)
                break
        # print("Conversion: ", conversion)
        i +=1
    # print("Original:", seed, "Full Conversion: ", conversion)
    # input()
    if conversion < lowestConversion:
        lowestConversion = conversion
print("Lowest location:", lowestConversion)
