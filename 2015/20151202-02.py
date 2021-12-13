import os
import math

# Advent of Code 2015
# Day 02 | Part 02
# https://adventofcode.com/2015/day/2

# set path to local folder
localFolder = os.getcwd() + "/2015/"

inputArr = []
testArr = [[1,1,10]]

# process input and push to array
with open(localFolder + '20151202input.txt', "r") as f:
  for line in f:
    tempArr = []
    stripped_line = line.strip()
    tempArr.append(int(stripped_line.split('x')[0]))
    tempArr.append(int(stripped_line.split('x')[1]))
    tempArr.append(int(stripped_line.split('x')[2]))
    inputArr.append(tempArr)

print(inputArr)

totalFeet = 0
for present in inputArr:
    present.sort()
    feetWrap = 2*present[0] + 2*present[1]
    feetBow = present[0]*present[1]*present[2]
    totalFeet += feetWrap + feetBow
    
print(totalFeet)