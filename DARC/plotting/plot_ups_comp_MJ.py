#!/usr/bin/env python
'''
@name: plot_ups_comp_MJ.py
@author: Matt
@date: Feb 28, 2014
@version: 1.0
@description: A python script for plotting the effective collision strengths for 
    a transition for the two cases of MB and MJ distribution averaging 
    on the same graph.

Input: plot_ups_comp_MJ.py [inputfile1] ["title"] { -s [outfile]}
'''

import numpy as np
import matplotlib.pyplot as plt
import sys
import math


def main(argv):
    '''Main function for module plot_transition'''
    if len(argv) < 2:
        raise Exception("Insufficient number of arguments")
    print(argv, len(argv))
    infile1 = argv[0]
    title = argv[1]
    save = False
    if len(argv) == 4:
        if argv[2] == '-s':
            save = True
            outfile = argv[3]

    # Load the input files and plot the appropriate columns
    data1 = np.loadtxt(infile1)
    #x2 = np.log10(data2[0:-2, 1])
    x1 = data1[0:-2, 1]
    y1 = data1[0:-2, 3]
    # Get theta values from the temperatures
    conver = 1.6863699549000089e-10
    theta = conver * x1
    # Calculate the MJ corrections and the corrected upsilons
    frel = f_rel(theta)
    y2 = frel * y1
    print(frel)
    # Create the desired uncertainty region
    err = 0.1 * y1
    fig, ax = plt.subplots(1)
    ax.plot(x1, y1, 'b--')
    ax.plot(x1, y2, 'r-')
    ax.fill_between(x1, y1 - err, y1 + err, alpha=0.3, edgecolor='blue',
            facecolor='blue')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlim([9e5,3e8])
    ax.set_ylim([1e-2,2e-2])
    ax.set_ylabel("$\\Upsilon$, Effective Collision Strength")
    ax.set_xlabel("$T \ (\mathrm{K})}$")
    ax.set_title(title)
    ax.legend(('MB Distribution', 'MJ Distribution'), loc='upper left',
              prop={'size': 10})
    if save:
        plt.savefig(outfile)
    else:
        plt.show()


def f_rel(t):
    return (1 / (1 + 15 * t / 8.0 + 105 * t**2 / 128.0
                - 945 * t**3 / 3072.0))


if __name__ == '__main__':
    main(sys.argv[1:])
