#!/usr/bin/env python
'''
@name: plot_upsilon_comp.py
@author: Matt
@date: Jan 20, 2014
@version: 1.0
@description: A python script for plotting the effective collision strengths for 
    transitions from different calculations on the same graph.

Input: plot_upsilon_comp.py [inputfile1] [inputfile2] ["title"] { -s [outfile]}
'''

import numpy as np
import matplotlib.pyplot as plt
import sys
import math


def main(argv):
    '''Main function for module plot_transition'''
    if len(argv) < 3:
        raise Exception("Insufficient number of arguments")
    print(argv, len(argv))
    infile1 = argv[0]
    infile2 = argv[1]
    title = argv[2]
    save = False
    if len(argv) == 5:  
        if argv[3] == '-s':
            save = True
            outfile = argv[4]

    # Load the input files and plot the appropriate columns
    data1 = np.loadtxt(infile1)
    data2 = np.loadtxt(infile2)
    lines = plt.plot(data1[:, 0], data1[:, 1], 'b-', 
            data2[:, 0], data2[:, 1], 'r--')
    plt.ylabel("Reduced Effective Collision Strength, $\\Upsilon_r$")
    plt.xlabel("Reduced Temperature, $T_r \ (\mathrm{K})$")
    plt.title(title)
    plt.legend(lines, ('DARC (n=3, 9 basis configurations)', 'BPICFT_Luis (n=7, 39 basis configurations'), loc='upper left', prop={'size':10})
    if save:
        plt.savefig(outfile)
    else:
        plt.show()

if __name__ == '__main__':
    main(sys.argv[1:])
