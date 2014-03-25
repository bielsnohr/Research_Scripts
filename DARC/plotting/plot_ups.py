#!/usr/bin/env python
'''
@name: plot_omega.py
@author: Matt
@date: Feb 26, 2014
@version: 1.0
@description: A python script for plotting the collision strength 

Input: plot_upsilon_comp.py [inputfile1] [inputfile2] ["title"] { -s [outfile]}
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
    fig, ax = plt.subplots(1)
    ax.plot(x1, y1, 'b-') 
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_xlim([9e5,2e8])
    #ax.set_ylim([1e-2,0.02])
    ax.set_ylabel("$\\Upsilon$, Effective Collision Strength")
    ax.set_xlabel("$T_e$ (K)")
    ax.set_title(title)
    #ax.legend('DARC (n=3, 9 basis configurations)')# prop={'size':10})
    if save:
        plt.savefig(outfile)
    else:
        plt.show()

if __name__ == '__main__':
    main(sys.argv[1:])
