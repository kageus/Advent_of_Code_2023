dataInput = open("../inputs/input_8").read().split("\n")
# dataInput = open("../inputs/sample_input_8.2").read().split("\n")

instructions = dataInput.pop(0).replace("L", "0").replace("R", "1")
dataInput.pop(0)
nodeDictionary = {}
for line in dataInput:
    pair = line.split(" = ")
    nodeDictionary[pair[0]] = pair[1].strip("()").split(", ")
currents = [key for key in nodeDictionary.keys() if key.endswith("A")]
print(currents)
steps = 0
hightest = 0
print(len(currents), currents)
input()
while not len([current for current in currents if current.endswith('Z')]) == len(currents):
    for char in instructions:
        currents = [nodeDictionary[current][int(char)] for current in currents]
        steps += 1
        if steps % 1000 == 0:
            print(f"{steps:,} steps and {hightest} highest found")
        if len([current for current in currents if current.endswith('Z')]) > hightest:
            hightest = len([current for current in currents if current.endswith('Z')])
        if len([current for current in currents if current.endswith('Z')]) == len(currents):
            break

print(currents)
print(steps)