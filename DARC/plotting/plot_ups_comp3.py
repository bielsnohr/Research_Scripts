#!/usr/bin/env python
'''
@name: plot_ups_comp3.py
@author: Matt
@date: Feb 14, 2014
@version: 1.0
@description: A python script for plotting the effective collision strengths for 
    transitions from 3 different calculations on the same graph.

Input: plot_upsilon_comp.py [inputfile1] [inputfile2] ["title"] { -s [outfile]}
'''

import numpy as np
import matplotlib.pyplot as plt
import sys
import math


def main(argv):
    '''Main function for module plot_transition'''
    if len(argv) < 4:
        raise Exception("Insufficient number of arguments")
    #print(argv, len(argv))
    infile1 = argv[0]
    infile2 = argv[1]
    infile3 = argv[2]
    title = argv[3]
    save = False
    if len(argv) == 6:  
        if argv[4] == '-s':
            save = True
            outfile = argv[5]

    # Load the input files and plot the appropriate columns
    data1 = np.loadtxt(infile1)
    data2 = np.loadtxt(infile2)
    data3 = np.loadtxt(infile3)
    #x2 = np.log10(data2[0:-2, 1])
    x1 = data1[0:-2, 1]
    y1 = data1[0:-2, 3]
    x2 = data2[0:-2, 1]
    y2 = data2[0:-2, 3]
    x3 = data3[0:-2, 0]
    y3 = data3[0:-2, 1]
    # Create the desired uncertainty region
    err = 0.2 * abs(y2)
    fig, ax = plt.subplots(1)
    ax.plot(x1, y1, 'b--') 
    ax.plot(x2, y2, 'g-*')
    ax.plot(x3, y3, 'r-')
    ax.fill_between(x2, y2 - err, y2 + err, alpha=0.5, edgecolor='green', 
            facecolor='green')
    ax.set_xscale('log')
    #ax.set_yscale('log')
    ax.set_ylabel("$\\Upsilon$, Effective Collision Strength")
    ax.set_xlabel("$T (\mathrm{K})$")
    ax.set_title(title)
    ax.legend(('DARC (n=3, 9 basis configs, MXE=54401)', 
        'BPICFT (n=7, 39 basis configs)', 'AUTOS DW'), loc='upper left', 
        prop={'size':10})
    if save:
        plt.savefig(outfile)
    else:
        plt.show()

if __name__ == '__main__':
    main(sys.argv[1:])
