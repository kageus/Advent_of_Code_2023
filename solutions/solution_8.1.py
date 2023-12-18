dataInput = open("../inputs/input_8").read().split("\n")
# dataInput = open("../inputs/sample_input_8_1_1").read().split("\n")
# dataInput = open("../inputs/sample_input_8_1_2").read().split("\n")

instructions = dataInput.pop(0).replace("L", "0").replace("R", "1")
dataInput.pop(0)
print(dataInput)
nodeDictionary = {}
for line in dataInput:
    pair = line.split(" = ")
    print(pair)
    nodeDictionary[pair[0]] = pair[1].strip("()").split(", ")

current = 'AAA'
count = 0
print(instructions)
while current != 'ZZZ':
    for char in instructions:
        current = nodeDictionary[current][int(char)]
        count += 1
        if current == 'ZZZ':
            break

print(count)