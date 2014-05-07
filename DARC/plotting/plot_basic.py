#!/usr/bin/env python
'''
@name: plot_basic.py
@author: Matt
@date: Jan 20, 2014
@version: 1.0
@description: A python script for plotting arbitrary column data. No fancy 
stuff.
'''

import numpy as np
import matplotlib.pyplot as plt
import sys
import math


def main(argv):
    '''
    Main function for module plot_basic
    
    input: [input file] [x column] [y column]
    '''
    if len(argv) < 3:
        raise Exception("Insufficient number of arguments")
    print(argv, len(argv))
    infile = argv[0]
    xcol = argv[1]
    ycol = argv[1]

    # Load the xout file and plot the appropriate columns
    data = np.loadtxt(infile)
    plt.plot(data[:-1, xcol], data[:-1, ycol], '-')
    plt.show()

if __name__ == '__main__':
    main(sys.argv[1:])
