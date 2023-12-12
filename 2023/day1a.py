import re

lines = open("day1a.txt", "r").readlines()

sum = 0

for line in lines:
    matchNumbers = re.findall("1|2|3|4|5|6|7|8|9|0", line)
    lineNumber = matchNumbers[0] + matchNumbers[-1]
    sum += int(lineNumber)

print(sum)