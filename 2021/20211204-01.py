import os
import itertools
import re

# Advent of Code 2021
# Day 04 | Part 01
# https://adventofcode.com/2021/day/4

# set path to local folder
localFolder = os.getcwd() + "/2021/"

inputArr = []

#filename = '20211204input.txt'
filename = '20211204input-sample.txt'

bingoNumbers = []
with open(localFolder + filename, "r") as file:
    linecount = 0
    for readline in file: 
        line_strip = readline.strip()
        
        if linecount == 0:
            bingoNumbers.append(line_strip.split(','))
    
        if linecount > 0 and line_strip != '':
            inputArr.append(line_strip)

        linecount += 1


cardsArr = []
for i in range(0, len(inputArr), 5):
    slice_item = slice(i, i + 5, 1)
    cardsArr.append(inputArr[slice_item])

rowArr = []
for card in cardsArr:
    rowArr.append(card[0].split())
    rowArr.append(card[1].split())
    rowArr.append(card[2].split())
    rowArr.append(card[3].split())
    rowArr.append(card[4].split())

print(rowArr)
