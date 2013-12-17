#!/usr/bin/env python
'''
@name: /Users/Matt/Google Drive/Python_workspace/Scripts/radiation_comp.py
@author: Matthew Bluteau
@date: Nov 27, 2013
@version: 1.0
@description: Simple script for reading in radiative data and creating
    comparison plots
'''

import numpy as np
import matplotlib.pyplot as plt
import sys
import math


def main(argv):
    # Load the data and get the min and max of the values being compared to
    data = np.loadtxt(argv[0])
    low = math.log(data[:, 6].min())
    high = math.log(data[:, 6].max())
    x = (low, high)
    y = (low, high)

    # Start plotting
    lines = plt.plot(x, y, 'k-', np.log(data[:, 6]), np.log(data[:, 0]), 'rx',
             np.log(data[:, 6]), np.log(data[:, 2]), 'b.')
    plt.ylabel('log($F_{kp-k}$(abs)) GRASP0')
    plt.xlabel('log($F_{kp-k}$(abs)) Fischer', labelpad=10)
    #plt.ylabel('log($S_{kp-k}$)) GRASP0')
    #plt.xlabel('log($S_{kp-k}$) Fischer', labelpad=10)
    plt.title('Comparison of Oscillator Absorption Strengths: GRASP0 vs. '
              'Fischer')
    plt.legend(lines, ('$y=x$', '$n=2$ opt', 'default'), loc='lower right')
    #plt.show()
    plt.savefig('fe22-comp_oscill_strength-02DEC2013.pdf')


if __name__ == '__main__':
    main(sys.argv[1:])
