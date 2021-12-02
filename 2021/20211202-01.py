import os


# Advent of Code 2021
# Day 02 | Part 01
# https://adventofcode.com/2021/day/2

# set path to local folder
localFolder = os.getcwd() + "/2021/"

commandsArr = []

# process input and push to array
with open(localFolder + '20211202input.txt', "r") as f:
  for line in f:
    stripped_line = line.strip()
    commandsArr.append(stripped_line)

horPos = 0
depth = 0
for command in commandsArr:
    direction = command.split(' ')[0]
    increment = command.split(' ')[1]
    
    if str(direction) == 'forward':
        horPos += int(increment)
    
    if str(direction) == 'down':
        depth += int(increment)
    
    if str(direction) == 'up':
        depth -= int(increment)

print("horizontal: " + str(horPos))
print("depth: " + str(depth))
print("product: " + str(horPos*depth))