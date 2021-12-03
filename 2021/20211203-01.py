import os
import itertools
import re

# Advent of Code 2021
# Day 03 | Part 01
# https://adventofcode.com/2021/day/3

# set path to local folder
localFolder = os.getcwd() + "/2021/"

inputArr = []
mostCommonArr = ''
leastCommonArr = ''
filename = '20211203input.txt'
#filename = '20211203input-sample.txt'

with open(localFolder + filename, "r") as f:
  for line in f:
    stripped_line = line.strip()
    inputArr.append(stripped_line)

#transpose the rows and columns
transposeArr = []
transposeArr = list(map(list, zip(*inputArr)))

# get the most and least common
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

# now convert to decimal from binary
gamma = int(mostCommonArr,2)
epsilon = int(leastCommonArr,2)
power = gamma*epsilon

print("gamma: " + str(gamma))
print("epsilon: " + str(epsilon))
print("power: " + str(power))