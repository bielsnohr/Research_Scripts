#!/usr/bin/env python
'''
@name: plot_omega_comp.py
@author: Matt
@date: Feb 5, 2014
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
    x1 = data1[0:-2, 1]
    y1 = data1[0:-2, 3]
    # For comparing upsilons from a DW calculation, use the conversion of the
    # temperature to energies in Ryd below
    x2 = 6.336273823529412e-06 * data2[0:-2, 0]
    # Otherwise, just keep things normal as below
    #x2 = data2[0:-2, 1]
    y2 = data2[0:-2, 1]

    # Create the desired uncertainty region
    # err = 0.2 * y2
    fig, ax = plt.subplots(1)
    ax.plot(x1, y1, 'r-') 
    ax.plot(x2, y2, 'b--')
    # ax.fill_between(x2, y2 - err, y2 + err, alpha=0.5, edgecolor='red', 
    #        facecolor='red')
    ax.set_ylabel("$\Omega$, Collision Strength")
    ax.set_xlabel("Scattered Energy, $E$ (Ryd)")
    ax.set_yscale("log")
    ax.set_ylim((1e-4,2))
    ax.set_xlim((0,450))
    ax.set_title(title)
    #ax.legend(('DARC (serial, MXE=6601)', 'DARC (parallel, MXE=54401)'), loc='upper right', prop={'size':10})
    #ax.legend(('DARC', 'BP ICFT'), loc='upper right', prop={'size':10})
    ax.legend(('BP ICFT $\Omega$', 'AUTOS DW $\\Upsilon$'), loc='upper right', prop={'size':10})
    if save:
        plt.savefig(outfile)
    else:
        plt.show()

if __name__ == '__main__':
    main(sys.argv[1:])
