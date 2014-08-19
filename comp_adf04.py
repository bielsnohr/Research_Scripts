#!/usr/bin/env python
'''
@name: comp_adf04.py
@author: MMB
@date: 2014-08-18
@version: 0.0
@description: A fairly rudimentary script for reading in two adf04 files and
    comparing them in various ways
'''

import numpy as np
import matplotlib.pyplot as plt
import sys
import math
#import subprocess as sp
#import os
import datetime as dt
import glob
import argparse as ap
import re


def main():
    '''
    Main function for purpose above
    '''
    # Open the two adf04 files
    adf = open('adf04', 'r')
    adfdamp = open('adf04-damp', 'r')
    # Discard the first line of each
    adf.readline()
    adfdamp.readline()
    adf_j = []
    #adfdamp_j = []
    regex1 = re.compile(' {2,}')
    regex2 = re.compile('\d+\.\d+')
    regex3 = re.compile('-1')

    # read in the J values for each level and check they match
    for line1, line2 in zip(adf, adfdamp):
        if regex3.search(line1) and regex3.search(line2):
            break
        if regex3.search(line1) or regex3.search(line2):
            print('Unequivalent level specification... quitting')
            return 1
        else:
            # get rid of encapsulating white space and split
            # the line if more than 2 spaces are present
            line1a = regex1.split(line1.lstrip().rstrip())
            l1 = line1a[0]
            j1 = regex2.search(line1a[2]).group() 
            line2a = regex1.split(line2.lstrip().rstrip())
            l2 = line2a[0]
            j2 = regex2.search(line2a[2]).group() 
            if j1 == j2 and l1 == l2:
                adf_j.append((l1, j1))
                #adfdamp_j.append((l2, j2))
            else:
                print('Unequivalent level specification... quitting')
                return 1


if __name__ == '__main__':
    main()
