import os
import itertools
import re

# Advent of Code 2021
# Day 07 | Part 01
# https://adventofcode.com/2021/day/7

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
dxArr = []
for i in range(0,len(inputArr)-1):
    diffArr = []
    for j in range(0,len(inputArr)):
        diffArr.append(abs(inputArr[i] - inputArr[j]))
    dxArr.append(diffArr)

# find the smallest rate of second order change
sumArr = []
for dx in dxArr:
    sumArr.append(sum(dx))

print(str(min(sumArr)))
