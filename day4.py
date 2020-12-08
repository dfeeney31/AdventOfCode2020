# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 18:37:26 2020

@author: Daniel.Feeney
"""

with open("C:/Users/Daniel.Feeney/Desktop/AdventOfCode2020/day4Input.txt") as f:
    data = f.read().split('\n\n')

passports = [d.replace('\n', ' ') for d in data]

passports = [{key: value for word in passport.split() for key, value in [word.split(':')]} for passport in passports]

validNo = 0
for entry in passports:
    if len(entry) == 8:
        validNo += 1
    elif (len(entry) == 7) and ('cid' not in entry):
        validNo += 1 
validNo

       
