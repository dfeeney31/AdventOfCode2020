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

#Solution 2
xSlopes = [1,3,5,7]
number_list = [ calcNoTrees(lines, x,0,1) for x in xSlopes ]
print(number_list)
import numpy as np
np.prod(number_list)

# traverse the Y slope 
ySlope = 2
currentX = 0
trees = 0
for currentLine in range(0,len(lines),ySlope):
    tmpLine = lines[currentLine]
    if tmpLine[currentX] == '#':
        trees =+ 1
    currentX = (currentX + 1) % 31
print(trees)

### online solution 
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
mult_trees=1
for slope in slopes:
    print("Slope: ", slope)
    slope_x, slope_y=slope
    trees = 0
    curr_x = 0
    for curr_y, each_line in enumerate(lines):
        if curr_y%slope_y == 0: #if current y equals slope 0, do nothing 

            if each_line[curr_x] == "#":
                trees+=1
            curr_x = (curr_x + slope_x) % len(each_line[:-1])
    print("Trees on this slope: ", trees)
    mult_trees*=trees
print("Solution 2: ", mult_trees)