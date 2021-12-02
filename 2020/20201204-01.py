import os
import itertools
import re

# Advent of Code 2020
# Day 04 | Part 01
# https://adventofcode.com/2020/day/4

# set path to local folder
localFolder = os.getcwd() + "/2020/"

inputArr = []
numLines = 0
numChars = 0
filename = '20201204input.txt'
#filename = '20201204input-sample.txt'

noBreak = ""
with open(localFolder + filename, "r") as file:
    
    for readline in file: 
        line_strip = readline.strip()
        if line_strip == '':
          noBreak += ','
        else:
          noBreak += line_strip
        
pwArray = noBreak.split(',')

passFieldsReqd = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:','cid:']
passFieldsOpt = ['cid']
numValid = 0
for pw in pwArray:
    if passFieldsReqd[0] in pw and passFieldsReqd[1] in pw and passFieldsReqd[2] in pw and passFieldsReqd[3] in pw and passFieldsReqd[4] in pw and passFieldsReqd[5] in pw and passFieldsReqd[6] in pw:
      numValid += 1


print(str(numValid))