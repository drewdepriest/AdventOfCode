import os
import itertools

# Advent of Code 2020
# Day 04 | Part 01
# https://adventofcode.com/2020/day/4

# set path to local folder
localFolder = os.getcwd() + "/2020/"

inputArr = []
numLines = 0
numChars = 0
with open(localFolder + '20201204input.txt', "r") as f:
  for line in f:
    tempArr = line.rstrip('\r\n') 
    tempArr = tempArr.split('\n \n')
    inputArr.append(tempArr)
    numLines += 1

lines = (line.rstrip() for line in open(localFolder + '20201204input.txt'))
for line in lines:
    tempArr2 = line.split('\n')
    print(tempArr2)

passFieldsReqd = ['byr','iyr','eyr','hgt','hcl''ecl','pid','cid']
passFieldsOpt = ['cid']

numValid = 0


print(str(numValid))