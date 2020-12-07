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

# solution 1 function 
def calcNoTrees(treeField, slopeX, currentX):

    trees = 0
    for yPosition, currentLine in enumerate(lines):
        if currentLine[currentX] == "#":
            trees+=1
        currentX = (currentX + slopeX) % len(currentLine[:-1])
    return trees

#Solution 1
xSlopes = [3]
number_list = [ calcNoTrees(lines, x, 0) for x in xSlopes ]
print(number_list)



# solution 2 function 

def calcNoTrees(treeField, slopeX, currentX, ySlope):
    
    trees = 0
    if ySlope == 1:
        for yPosition, currentLine in enumerate(lines):            
            if currentLine[currentX] == "#":
                trees+=1
            currentX = (currentX + slopeX) % len(currentLine[:-1])
            
    # this part not working         
    elif ySlope != 1:
        for currentLine in range(0,len(lines),ySlope):
            if currentLine[currentX] == '#':
                trees =+ 1
            currentX = (currentX + slopeX) % len(currentLine[:-1])
    return trees

ySlope = 2
currentX = 0
trees = 0
for currentLine in range(0,len(lines),ySlope):
    tmpLine = lines[currentLine]
    currentX = currentX % len(tmpLine[:-1])
    if tmpLine[currentX] == '#':
        trees =+ 1
print(trees)

#Solution 2
xSlopes = [1,3,5,7]
number_list = [ calcNoTrees(lines, x,0,1) for x in xSlopes ]
print(number_list)
import numpy as np
np.prod(number_list)
