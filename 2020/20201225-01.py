import os
import itertools
import re

# Advent of Code 2020
# Day 25 | Part 01
# https://adventofcode.com/2020/day/25

## SAMPLE ##
#cardKeyPub = 5764801
#doorKeyPub = 17807724

## ACTUAL ##
cardKeyPub = 18499292
doorKeyPub = 8790390

subjectNum = 7
modValue = 20201227
loopSizeCard = 1
loopSizeDoor = 1

# get card's loop size
cardCount = 0
while loopSizeCard != cardKeyPub:
    loopSizeCard = loopSizeCard * subjectNum
    loopSizeCard = loopSizeCard%modValue
    cardCount += 1

loopSizeCard = cardCount

# get door's loop size
doorCount = 0
while loopSizeDoor != doorKeyPub:
    loopSizeDoor = loopSizeDoor * subjectNum
    loopSizeDoor = loopSizeDoor%modValue
    doorCount += 1

loopSizeDoor = doorCount

## Transforming door pub key with card loop size yields shared encryption key
encryptKey = 1
loop = 0
while loop < loopSizeCard:
    encryptKey = encryptKey * doorKeyPub
    encryptKey = encryptKey%modValue
    loop += 1
print(encryptKey)

## Transforming card pub key with door loop size yields shared encryption key
encryptKey = 1
loop = 0
while loop < loopSizeDoor:
    encryptKey = encryptKey * cardKeyPub
    encryptKey = encryptKey%modValue
    loop += 1
print(encryptKey)