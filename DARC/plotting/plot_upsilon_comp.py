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
    #x2 = np.log10(data2[0:-2, 1])
    x1 = data1[0:-2, 1]
    y1 = data1[0:-2, 3]
    x2 = data2[0:-2, 1]
    y2 = data2[0:-2, 3]
    # Create the desired uncertainty region
    err = 0.2 * y2
    fig, ax = plt.subplots(1)
    ax.plot(x1, y1, 'b--') 
    ax.plot(x2, y2, 'r-') 
    ax.fill_between(x2, y2 - err, y2 + err, alpha=0.5, edgecolor='red', 
            facecolor='red')
    ax.set_xscale('log')
    ax.set_ylabel("$\\Upsilon$, Effective Collision Strength")
    ax.set_xlabel("$\log_{10}{[T \ (\mathrm{K})]}$")
    ax.set_title(title)
    ax.legend(('DARC (n=3, 9 basis configurations)', 'BPICFT_Luis (n=7, 39 basis configurations'), loc='lower left', prop={'size':10})
    if save:
        plt.savefig(outfile)
    else:
        plt.show()

if __name__ == '__main__':
    main(sys.argv[1:])
