import os


# Advent of Code 2021
# Day 01 | Part 01
# https://adventofcode.com/2021/day/1

# set path to local folder
localFolder = os.getcwd() + "/2021/"

depthArr = []

# process input and push to array
with open(localFolder + '20211201-01input.txt', "r") as f:
  for line in f:
    stripped_line = line.strip()
    depthArr.append(int(stripped_line))

# look for increase in value from one index to next
increase = 0
for previous, current in zip(depthArr, depthArr[1:]):
    if current > previous:
        increase += 1

#print the solution
print(increase)
