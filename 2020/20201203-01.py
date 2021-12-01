import os
import itertools

# Advent of Code 2020
# Day 03 | Part 01
# https://adventofcode.com/2020/day/1

# set path to local folder
localFolder = os.getcwd() + "/2020/"

inputArr = []
numLines = 0
numChars = 0
with open(localFolder + '20201203input.txt', "r") as f:
  for line in f:
    stripped_line = line.strip()
    numChars = len(stripped_line)
    inputArr.append(stripped_line)
    numLines += 1

# open squares (.)  
# trees (#)
square = '.'
tree = '#'

# slope: right 3, down 1
slopeRight = 1
slopeDown = 2
numTrees = 0
counter = 0

while counter < numLines:
    nextMove = str(inputArr[counter][(counter*slopeRight)%numChars]) 
    if nextMove == tree:
        numTrees += 1
    counter += slopeDown

print(int(numTrees))