#!/usr/bin/env python
'''
@name: plot_transition_upsilon.py
@author: Matt
@date: Jan 20, 2014
@version: 1.0
@description: A python script for plotting the effective collision strengths for 
    transitions in an upsout file derived from an adf04 file
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
    infile = argv[0]
    title = argv[1]
    save = False
    if len(argv) == 4:  
        if argv[2] == '-s':
            save = True
            outfile = argv[3]

    # Load the xout file and plot the appropriate columns
    data = np.loadtxt(infile)
    plt.plot(data[0:-2, 1], data[0:-2, 3], '-')
    plt.ylabel("$\\Upsilon$, Effective Collision Strength")
    plt.xlabel("Temperature (K)")
    plt.title(title)
    if save:
        plt.savefig(outfile)
    else:
        plt.show()

if __name__ == '__main__':
    main(sys.argv[1:])
