import os
import itertools
import re

# Advent of Code 2021
# Day 03 | Part 02
# https://adventofcode.com/2021/day/3#part2

# set path to local folder
localFolder = os.getcwd() + "/2021/"

inputArr = []

#filename = '20211203input.txt'
filename = '20211203input-sample.txt'

with open(localFolder + filename, "r") as f:
  for line in f:
    stripped_line = line.strip()
    inputArr.append(stripped_line)

#transpose the rows and columns
def transpose(arr):
    tempArr = []
    tempArr = list(map(list, zip(*arr)))
    return tempArr

# get the most and least common
def getCommon(arr,type):
    mostCommonArr = ''
    leastCommonArr = '' 
    for cols in transposeArr:
        count0 = 0
        count1 = 0
        for item in cols:
            if item == '0':
                count0 += 1
            if item == '1':
                count1 += 1
        if count1 > count0:
            mostCommonArr += '1'
            leastCommonArr += '0'
        else:
            mostCommonArr += '0'
            leastCommonArr += '1'
    
    if type == 'most':
        return mostCommonArr
    if type == 'least':
        return leastCommonArr

transposeArr = transpose(inputArr)
mostCommon = getCommon(inputArr,'most')
leastCommon = getCommon(inputArr,'least')

oxygen = ''
co2 = ''

for i in range(len(inputArr)):
    getCommon(inputArr,'most')

colCount = 0
mostCommon = getCommon(inputArr,'most')
popRows = []
while colCount < len(inputArr[0]):
    rowCount = 0
    while rowCount < len(inputArr):
        if inputArr[rowCount][colCount] == mostCommon[colCount]:
            popRows.append(rowCount)
        rowCount += 1 

    colCount += 1

print(inputArr)

# now convert to decimal from binary
gamma = int(mostCommon,2)
epsilon = int(leastCommon,2)
power = gamma*epsilon

print("gamma: " + str(gamma))
print("epsilon: " + str(epsilon))
print("power: " + str(power))

