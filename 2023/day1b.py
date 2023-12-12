lines = open("day1b.input.txt", "r").readlines()

value_list = {"1","2","3","4","5","6","7","8","9","one","two", "three", "four", "five", "six", "seven", "eight", "nine"}


def getFirstValue(word):
    lowestMatchValue = ""
    lowestIndexMatch = len(word)

    for value in value_list:
        currentMatchIndex = word.find(value)

        if(currentMatchIndex > -1 and currentMatchIndex < lowestIndexMatch ):
            lowestMatchValue = value
            lowestIndexMatch = currentMatchIndex

    return getWordValue(lowestMatchValue)


def getLastValue(word):

    highestMatchValue = ""
    highestIndexMatch = -1

    for value in value_list:
        currentMatchIndex = word.rfind(value)

        if(currentMatchIndex > -1 and currentMatchIndex > highestIndexMatch ):
            highestMatchValue = value
            highestIndexMatch = currentMatchIndex

    return getWordValue(highestMatchValue)


def getWordValue(word):

    value = ""

    match word:
        case "one":
            value = "1"
        case "two":
            value = "2"
        case "three":
            value = "3"
        case "four":
            value = "4"
        case "five":
            value = "5"
        case "six":
            value = "6"
        case "seven":
            value = "7"
        case "eight":
            value = "8"
        case "nine":
            value = "9"
        case _:
            value = word

    return value


sum = 0

print("------------------------ START ----------------------------")
for line in lines:
    combined_value = getFirstValue(line) +  getLastValue(line)            
    sum += int(combined_value)

print(sum)