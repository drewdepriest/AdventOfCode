import os


# Advent of Code 2021
# Day 01 } Part 02
# https://adventofcode.com/2021/day/1

# set path to local folder
localFolder = os.getcwd() + "/2021/"

depthArr = []

with open(localFolder + '20211201-01input.txt', "r") as f:
  for line in f:
    stripped_line = line.strip()
    depthArr.append(int(stripped_line))

windowsum = 0
windowsumArr = []
for minusone, minustwo, current in zip(depthArr, depthArr[1:],depthArr[2:]):
    windowsum = minusone+minustwo+current
    windowsumArr.append(windowsum)

increase = 0
for previous, current in zip(windowsumArr, windowsumArr[1:]):
    if current > previous:
        increase += 1

print(increase)