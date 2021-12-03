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
print(pwArray)

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
validECL = ['amb','blu','brn','gry','grn','hzl','oth']
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

def hgt(pw):
    tempStr = pw.split('hgt:')[1].split(' ')[0]
    tempUnits = tempStr[-2:]
    tempVal = tempStr[:-2]

    if tempUnits == 'in' and int(tempVal) >= 59 and int(tempVal) <= 76:
       return 'true'
    elif tempUnits == 'cm' and int(tempVal) >= 150 and int(tempVal) <= 193:
       return 'true'
    else:
        return 'false'

def hcl(pw):
    charAllowed = "0123456789abcdef"
    charOne = pw.split('hcl:')[1][0]
    charString = str(pw.split('hcl:')[1][1:7])

    if charOne == '#' and all(c in charAllowed for c in charString):
       return 'true'  

def ecl(pw):
    ecl = pw.split('ecl:')[1][0:3]
    count = 0
    for valid in validECL:
        if ecl == valid:
            count += 1
        
    if count == 1:
        return 'true'

def pid(pw):
    pid = pw.split('pid:')[1][0:9]
    if str(pid).isnumeric() and len(pid) == 9:
        return 'true'

# are the fields present?
countPw = 0
for pw in pwArray:
    if passFieldsReqd[0] in pw and passFieldsReqd[1] in pw and passFieldsReqd[2] in pw and passFieldsReqd[3] in pw and passFieldsReqd[4] in pw and passFieldsReqd[5] in pw and passFieldsReqd[6] in pw and byr(pw) and iyr(pw) and eyr(pw) and hgt(pw) and hcl(pw) and ecl(pw) and pid(pw):
        #print(pw)
        #print('\n')
        numValid += 1
           
    countPw += 1
print("valid: " + str(numValid))