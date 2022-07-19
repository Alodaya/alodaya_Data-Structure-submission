#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:21:23 2022

@author: ainish
"""

def ProcessInput(fname = 1):
    Guards = []
    fname = 'input/' + str(fname) + '.in'
    with open(fname) as f:
        lines = f.readlines()
        lines.pop(0)

        for line in lines:
            SS = str.split(line)
            Guards.append ([int(SS[0]), int(SS[1])])
        Guards.sort(key = lambda X: X[0])
    return Guards

def WriteOutput(fname = 1, src = '', content = 'None'):
    fname = 'output/'+str(fname) + src + '.out'
    f = open(fname,'w')
    f.write(str(content))
    f.close
    return

                
