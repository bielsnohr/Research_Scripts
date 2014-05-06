#!/usr/bin/env python
'''
@name: /Users/Matt/Google Drive/Python_workspace/Research_Scripts/Emesh.py
@author: Matt
@date: Feb 12, 2014
@version: 1.0
@description: Basic python script for calculating the mesh parameters for a
    R-matrix STGF run
'''


import sys


def calc_params(argv):
    '''
    The main function that carries out the mesh parameters calculations
    given the start point, end point, and number of energy points as input.
    The output is E_0 (i.e. first energy point), EINCR (the energy step), and
    MXE (the number of energy points)
    '''
    Ei, Ef, MXE = argv
    Ei = float(Ei)
    Ef = float(Ef)
    MXE = int(MXE)
    EINCR = (Ef - Ei) / (MXE - 3)
    E0 = Ei - EINCR
    print("E0=" + str(E0) + ", " + "MXE=" + str(MXE) + ", " + "EINCR=" +
          str(EINCR))

if __name__ == '__main__':
    calc_params(sys.argv[1:])
