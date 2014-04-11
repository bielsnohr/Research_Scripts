#!/usr/bin/env python
'''
@name: /Users/Matt/Google Drive/Python_workspace/Research_Scripts/check_interval.py
@author: Matthew Bluteau
@date: 10/04/2014
@version: 1.0
@description: A python module for determining the minimum number of points between 
    nodes of basis orbitals produced by DARC stg1d_orbs
'''

import numpy as np
import glob


def main():
    '''
    Main function for module check_interval. No input. Checks all files named 
    bas* and orb*
    '''
    bas = glob.glob('bas*')
    orb = glob.glob('orb*')
    bas.sort()
    orb.sort()

    for i in bas + orb:
        print('------------------------')
        print('Search results in ', i)
        try:
            tmpf = np.loadtxt(i)
        except ValueError:
            print('There is an incorrectly formatted number in file, ', i)
            print('Skipping this file...')
            continue
        count = 1
        prev = tmpf[0, 1]
        for j in tmpf[1:, 1]:
            if (j < 0 and prev > 0) or (j > 0 and prev < 0):
                #print j, prev
                #print(count)
                if count < 15:
                    print('An instance of less than 15 mesh points between '
                            'nodes in file/orbital: ', i) 
                    print('Count: ', count)
                count = 1
            else:
                count += 1
            prev = j

if __name__ == '__main__':
    main()
