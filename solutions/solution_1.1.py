# dataInput = open("../inputs/input_1").read().split("\n")
dataInput = open("../inputs/sample_input_1.1").read().split("\n")

codeList = []
for line in dataInput:
    codeList.append(str(line))

currentSum = 0
print(f"\n   {currentSum}")
for code in codeList:
    for c in code:
        if(c.isdigit()):
            firstDigit = c
            break
    for c in reversed(code):
        if(c.isdigit()):
            secondDigit = c
            break
    combinedDigits = int(firstDigit + secondDigit)
    print(f"+  {firstDigit}{secondDigit}")
    currentSum += combinedDigits
    print(f"=  {currentSum}\n")
print(f"Final Sum: {currentSum}")