import os
import math

# Advent of Code 2019
# Day 01 | Part 02
# https://adventofcode.com/2019/day/1#part2

# set path to local folder
localFolder = os.getcwd() + "/2019/"

inputArr = []

# process input and push to array
with open(localFolder + '20191201-01input.txt', "r") as f:
  for line in f:
    stripped_line = line.strip()
    inputArr.append(int(stripped_line))

#print(inputArr)
part01Mass = 0

# get the mass
for input in inputArr:
    mass = math.floor(input/3) - 2
    part01Mass += mass

print(part01Mass)

testArr = [14,1969,100756]

def getTotalMass(mass):
    mass = math.floor(mass/3) - 2
    return mass

# get the fuel mass from each block of fuel
fuelMassArr = []
for input in inputArr:
    mass = input
    totalMass = 0
    while getTotalMass(mass) > 0:
        mass = getTotalMass(mass)
        totalMass = totalMass + mass
    fuelMassArr.append(totalMass)

# now sum everything in the fuelMass array
fuelSum = 0
for fuelMass in fuelMassArr:
    print(fuelMass)
    fuelSum = fuelSum + fuelMass

print(fuelSum)