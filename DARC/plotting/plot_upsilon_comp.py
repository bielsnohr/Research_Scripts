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
    #title = argv[2]
    lev1 = argv[2]
    lev2 = argv[3]
    save = False
    if len(argv) == 6:  
        if argv[4] == '-s':
            save = True
            outfile = argv[5]

    lev = {'1':'3d^{10}\!4s^2 \ ^1\!S_0^{\circ}', '275':\
            '3d^{9}\!4s^2\!4f \ \ ^3\!D_1^{\circ}', '290':\
            '3d^{9}\!4s^2\!4f \ \ ^1\!P_1^{\circ}', '295':\
            '3d^{9}\!4s^2\!4f \ \ ^3\!P_1^{\circ}'}
    title = 'Transition ' + lev1 + '-' + lev2 + ', $' + lev[lev1] +\
            '\\rightarrow' + lev[lev2] + '$'
    # Load the input files and plot the appropriate columns
    data1 = np.loadtxt(infile1)
    data2 = np.loadtxt(infile2)
    #x2 = np.log10(data2[0:-2, 1])
    x1 = data1[0:-2, 0]
    y1 = data1[0:-2, 1]
    x2 = data2[0:-2, 0]
    y2 = data2[0:-2, 1]
    # Create the desired uncertainty region
    err = 0.1 * y2
    fig, ax = plt.subplots(1)
    ax.plot(x1, y1, 'b--') 
    ax.plot(x2, y2, 'r-') 
    ax.fill_between(x2, y2 - err, y2 + err, alpha=0.2, edgecolor='red', 
            facecolor='red')
    ax.set_xscale('log')
    ax.set_ylabel("$\\Upsilon$, Effective Collision Strength")
    ax.set_xlabel("$T \ (\mathrm{K})$")
    ax.set_title(title)
    ax.legend(('W+44 AS DW MENGI=-1', 'W+44 AS DW MENGI=-2'), loc='upper left', prop={'size':10})
    if save:
        plt.savefig(outfile)
    else:
        plt.show()

if __name__ == '__main__':
    main(sys.argv[1:])
