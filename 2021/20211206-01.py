import os
import itertools
import re

# Advent of Code 2021
# Day 06 | Part 01
# https://adventofcode.com/2021/day/3

# set path to local folder
localFolder = os.getcwd() + "/2021/"

inputArr = []
days = 80
filename = '20211206input.txt'
#filename = '20211206input-sample.txt'

with open(localFolder + filename, "r") as f:
    inputArr = f.read().split(',')

# convert to int
inputArr = [int(i) for i in inputArr]

# subtract 1 from every value in array
def subtractFish(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] - 1
        if arr[i] == -1:
            arr[i] = 6
            arr.append(8)

    return arr

count = 0
tempArr = inputArr
print(tempArr)
while count < days:
    tempArr = subtractFish(tempArr)
    count += 1
    print(tempArr)

print("total fish: " + str(len(tempArr)))