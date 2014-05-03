#!/usr/bin/env python
'''
@name: /Users/Matt/Google Drive/Python_workspace/Research_Scripts/plot_bas.py
@author: Matt
@date: Dec 16, 2013
@version: 1.0
@description: A python module for plotting the basis orbitals produced by the
    DARC stage stg1d_orbs. The bound input orbitals and constructed continuum
    orbitals are each given in groups of 10.
'''

import numpy as np
import matplotlib.pyplot as plt
import sys
import math


def main(argv):
    '''Main function for module plot_bas'''
    try:
        if len(argv) < 4:
            raise Exception("Insufficient arguments specified. Min of 4.")
        temp_args = argv[0:4]
        for i in temp_args:
            int(i)
    except Exception as exc:
        print(exc)
        raise
    except ValueError:
        print("First four argument must be numbers. Conversion to ints failed.")
        raise
    else:
        orb_low = int(argv[0])
        orb_high = int(argv[1])
        bas_low = int(argv[2])
        bas_high = int(argv[3])
        save = False
        if len(argv) > 4:  
            if argv[4] == '-s':
                save = True

    # Print the bound orbitals in groups of 10
    count = 0
    plot_count = 1
    for i in range(orb_low, orb_high):
        if count % 10 == 0:
            plt.figure(plot_count)
            plot_count += 1
        count += 1
        index = str(i).rjust(3, '0')
        file = 'orb' + index
        data = np.loadtxt(file)
        plt.plot(data[:, 0], data[:, 1], '-')
    plt.show()

    # Print the bound orbitals in groups of 10
    count = 0
    for i in range(bas_low, bas_high):
        if count % 10 == 0:
            plt.figure(plot_count)
            plot_count += 1
        count += 1
        index = str(i).rjust(3, '0')
        file = 'bas' + index
        data = np.loadtxt(file)
        plt.plot(data[:, 0], data[:, 1], '-')
    plt.show()

if __name__ == '__main__':
    main(sys.argv[1:])