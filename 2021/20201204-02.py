import os
import itertools
import re

# Advent of Code 2020
# Day 04 | Part 02
# https://adventofcode.com/2020/day/4#part2

# set path to local folder
localFolder = os.getcwd() + "/2020/"

inputArr = []
numLines = 0
numChars = 0
#filename = '20201204input.txt'
filename = '20201204input-sample.txt'

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
numPresent = 0
numValid = 0

validBYR = [4,1920,2002]
validIYR =[4,2010,2020]
validEYR = [4,2020,2030]
validHGTcm =  ["cm",150,193]
validHGTin = ["in",59,76]
validHCL = ["#",6]
validECL = ['amb','blue','brn','gry','grn','hzl','oth']
validPID = 9

def byr(pw):
    tempStr = pw.split('byr:')[1][0:4]
    if int(tempStr) >= validBYR[1] and int(tempStr) <= validBYR[2]:
        return 'true'

def iyr(pw):
    tempStr = pw.split('iyr:')[1][0:4]
    if int(tempStr) >= validIYR[1] and int(tempStr) <= validIYR[2]:
        return 'true'

def eyr(pw):
    tempStr = pw.split('eyr:')[1][0:4]
    if int(tempStr) >= validEYR[1] and int(tempStr) <= validEYR[2]:
        return 'true'

# are the fields present?
for pw in pwArray:
    if passFieldsReqd[0] in pw and passFieldsReqd[1] in pw and passFieldsReqd[2] in pw and passFieldsReqd[3] in pw and passFieldsReqd[4] in pw and passFieldsReqd[5] in pw and passFieldsReqd[6] in pw:
        numPresent += 1
        if(byr(pw)):
          print("BYR is valid")

        if(iyr(pw)):
          print("IYR is valid")

        if(eyr(pw)):
          print("EYR is valid")

      # are the fields valid?



#print(str(numValid))