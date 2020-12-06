# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:26:37 2020

@author: Daniel.Feeney
"""    

def passwordLegit(line):
    # first break out the letter and number of times required
    policy, password = [item.strip() for item in line.split(':')]
    bounds = policy[:-2]
    letter = policy[-1]
    low, high = [int(item) for item in bounds.split('-')]
    
    return (password.count(letter) >= low) & (password.count(letter) <= high)


def passwordLegitComplex(line):
    # first break out the letter and number of times required
    policy, password = [item.strip() for item in line.split(':')]
    indices = policy[:-2]
    letter = policy[-1]
    low, high = [int(item) for item in indices.split('-')]
    
    if (password[low-1] == letter) & (password[high-1] != letter):
        return True
    elif (password[low-1] != letter) & (password[high-1] == letter):
        return True
    return False
    

data = []
trueFalse = []
totalGood = 0
with open("C:/Users/Daniel.Feeney/Desktop/AdventOfCode2020/day2Input.txt") as f:
    for line in f:
        data.append(line.strip())
        if passwordLegitComplex(line):
            totalGood += 1
        
