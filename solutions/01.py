import re
import os

script_dir = os.path.dirname(__file__)
rel_path = '../inputs/01.txt'

file = open(os.path.join(script_dir, rel_path), 'r', encoding='utf-8')

numberStringDict = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}

combinedNumberStringDict = {}

for key1, value1 in numberStringDict.items():
    for key2, value2 in numberStringDict.items():
        if key1[0] == key2[-1]:
            combinedNumberStringDict[key2 + key1[1:]] =  value2 + value1
        if key1[-1] == key2[0]:
            combinedNumberStringDict[key1 + key2[1:]] = value1 + value2
    combinedNumberStringDict[key1] = value1

sum1 = 0

for line in file:
    onlyNumbers = re.sub(r'[a-zA-Z]', '', line).strip()

    if len(onlyNumbers) != 0:
        sum1 += int(onlyNumbers[0] + onlyNumbers[-1])

print('Part 1:', sum1)

file.seek(0)
sum2 = 0

for line in file:
    for key, value in combinedNumberStringDict.items():
        line = line.replace(key, str(value))

    onlyNumbers = re.sub(r'[a-zA-Z]', '', line).strip()

    if len(onlyNumbers) != 0:
        sum2 += int(onlyNumbers[0] + onlyNumbers[-1])

print('Part 2:', sum2)

file.close()
