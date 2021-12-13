import os
import math

# Advent of Code 2015
# Day 01 | Part 02
# https://adventofcode.com/2015/day/1#part2

# set path to local folder
localFolder = os.getcwd() + "/2015/"

inputArr = []

# process input and push to array
floors = 0
index = 0
with open(localFolder + '20151201input.txt', "r") as f:
  for line in f:
    for char in line:
        if char == "(":
            floors += 1
        if char == ")":
            floors -= 1
        index += 1
        if floors == -1:
            print(index)

print(floors)
print(index)