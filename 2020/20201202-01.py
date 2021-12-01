import os
import itertools

# Advent of Code 2020
# Day 02 | Part 01
# https://adventofcode.com/2020/day/2

# set path to local folder
localFolder = os.getcwd() + "/2020/"

inputArr = []

with open(localFolder + '20201202input.txt', "r") as f:
  for line in f:
    stripped_line = line.strip()
    inputArr.append(stripped_line)

# build arrays of each field
fullList = []
for input in inputArr:
    rowList = []
    numLo = int((str(input).split(':')[0].split(' ')[0].split('-')[0]))
    numHi = int((str(input).split(':')[0].split(' ')[0].split('-')[-1]))
    char = str(input).split(':')[0].split(' ')[1]
    password = str(input).split(' ')[-1]
    rowList.append(numLo)
    rowList.append(numHi)
    rowList.append(char)
    rowList.append(password)
    fullList.append(rowList)

totalCount = 0
for list in fullList:
    # rowArr[0] = lo/hi range
    # rowArr[1] = char
    # rowArr[2] = pw
    numLo = int(list[0])
    numHi = int(list[1])
    char = list[2]
    password = list[3]

    charCount = password.count(char)
    if charCount >= numLo and charCount <= numHi:
        totalCount = totalCount + 1

print(str(totalCount))