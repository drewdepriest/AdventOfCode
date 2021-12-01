import os
import itertools

# Advent of Code 2020
# Day 01 | Part 01
# https://adventofcode.com/2020/day/1

# set path to local folder
localFolder = os.getcwd() + "/2020/"

arr = []

with open(localFolder + '20201201input.txt', "r") as f:
  for line in f:
    stripped_line = line.strip()
    arr.append(int(stripped_line))

prod = 0
for numbers in itertools.combinations(arr,2):
    if sum(numbers) == 2020:
        prod = numbers[0]*numbers[1]
        print("product: " + str(prod)