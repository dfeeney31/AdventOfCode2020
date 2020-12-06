# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 11:33:13 2020

@author: Daniel.Feeney
"""

with open("C:/Users/Daniel.Feeney/Desktop/AdventOfCode2020/day3Input.txt", 'r') as f:
    lines=f.readlines()

# parameters        
currentX = 0
slopeX = 3
slopeY = 1

## Each line is 32 long, so each time you get to an X position of 32, 
## the next x index is 0 + remainder in the X position 

# preallocate trees
trees = 0
for yPosition, currentLine in enumerate(lines):
    if currentLine[currentX] == "#":
        trees+=1
    currentX = (currentX + slopeX) % len(currentLine[:-1])
print(f"Solution 1:{trees}")

