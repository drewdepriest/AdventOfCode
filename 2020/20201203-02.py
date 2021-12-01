import os
import itertools

# Advent of Code 2020
# Day 03 | Part 01
# https://adventofcode.com/2020/day/3#part2

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

#####
##### Now, check (5) different slopes and keep running product of all trees
#####

# slope[] = [right,down]
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

prodTrees = 1

for slope in slopes:
    numTrees = 0
    counter = 0
    while counter < numLines:
        
        nextMove = str(inputArr[counter][(counter*slope[0])%numChars]) 
        if nextMove == tree:
            numTrees += 1
        counter += slope[1]
        
    prodTrees = prodTrees*numTrees
    print("sumtrees: " + str(numTrees))
print("prodtree: " + str(prodTrees))
