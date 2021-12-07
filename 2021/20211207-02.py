import os
import itertools
import re

# Advent of Code 2021
# Day 07 | Part 02
# https://adventofcode.com/2021/day/7#part2

# set path to local folder
localFolder = os.getcwd() + "/2021/"

inputArr = []
days = 80
filename = '20211207input.txt'
#filename = '20211207input-sample.txt'

with open(localFolder + filename, "r") as f:
    inputArr = f.read().split(',')

# convert to int
inputArr = [int(i) for i in inputArr]

# get the second order changes
# allow for ANY horizontal position, not just those in the input array
dxArr = []
for i in range(0,max(inputArr)):
    diffArr = []
    for j in range(0,len(inputArr)):
        stepDiff = 0
        stepDiff = abs(inputArr[j] - i)
        stepDiff = ((stepDiff*stepDiff) + stepDiff)/2
        diffArr.append(stepDiff)
    dxArr.append(diffArr)

# find the smallest rate of step order change
sumArr = []
for dx in dxArr:
    sumArr.append(sum(dx))

print(str(min(sumArr)))
