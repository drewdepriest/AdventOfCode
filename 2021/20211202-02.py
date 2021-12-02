import os


# Advent of Code 2021
# Day 02 | Part 02
# https://adventofcode.com/2021/day/2#part2

# set path to local folder
localFolder = os.getcwd() + "/2021/"

commandsArr = []

# process input and push to array
with open(localFolder + '20211202input.txt', "r") as f:
  for line in f:
    stripped_line = line.strip()
    commandsArr.append(stripped_line)

testArr = ["forward 5","down 5","forward 8","up 3","down 8","forward 2"]

horPos = 0
depth = 0
aim = 0
for command in commandsArr:
    direction = command.split(' ')[0]
    increment = command.split(' ')[1]
    
    if str(direction) == 'forward':
        horPos += int(increment)
        depth = depth + aim*int(increment)
        print("aim: " + str(aim))
        print("depth: " + str(depth))
    
    if str(direction) == 'down':
        #depth += int(increment)
        aim += int(increment)
        print("aim: " + str(aim))
        print("depth: " + str(depth))
    
    if str(direction) == 'up':
        #depth -= int(increment)
        aim -= int(increment)
        print("aim: " + str(aim))
        print("depth: " + str(depth))

print("horizontal: " + str(horPos))
print("depth: " + str(depth))
print("product: " + str(horPos*depth))