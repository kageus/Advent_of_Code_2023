dataInput = open("../inputs/input_1").read().split("\n")
# dataInput = open("../inputs/sample_input_1.2").read().split("\n")

codeList = []
for line in dataInput:
    codeList.append(str(line))

findList                = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
conversionDictionary    = {"1": 1, "2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

currentSum = 0
print(f"\n   {currentSum}")
for code in codeList:
    # firstCode
    firstIndex = len(code)-1
    firstCode = 0
    for needle in findList:
        index = code.find(needle)
        if index != -1 and index <= firstIndex:
            firstIndex = index
            firstCode = conversionDictionary[needle]
    
    # secondCode
    lastIndex = 0
    lastCode = 0
    for needle in findList:
        index = code.rfind(needle)
        if index != -1 and index >= lastIndex:
                lastIndex = index
                lastCode = conversionDictionary[needle]
    
    print(code)
    combinedDigits = int(str(firstCode) + str(lastCode))
    print(f"{firstCode} {lastCode} or {combinedDigits} + {currentSum} =")
    currentSum += combinedDigits
    print(f"{currentSum}\n")

    # choice = input("n to break")
    # if choice == 'n':
    #      break
    
print(f"Final Sum: {currentSum}")