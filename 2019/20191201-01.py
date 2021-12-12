import os
import math

# Advent of Code 2019
# Day 01 | Part 01
# https://adventofcode.com/2019/day/1

# set path to local folder
localFolder = os.getcwd() + "/2019/"

inputArr = []

# process input and push to array
with open(localFolder + '20191201-01input.txt', "r") as f:
  for line in f:
    stripped_line = line.strip()
    inputArr.append(int(stripped_line))

print(inputArr)
totalMass = 0

# get the mass
for input in inputArr:
    mass = math.floor(input/3) - 2
    totalMass += mass

print(totalMass)