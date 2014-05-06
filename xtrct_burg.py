#!/usr/bin/env python
'''
@name: xtrct_burg.py
@author: Matt
@date: 2014-05-02
@version: 1
@description: A python script for creating Burgess-Tully scaled data from 
    upsilon transition data that has already been extracted by xtrct_trans.py
'''
import sys
import subprocess as sp
#import os
#import datetime as dt
import glob
import os


def main(argv):
    '''
    Main function for the xtrct_burg.py module
    Input/Usage: [om, ups] 
    '''
    #AS = True
    if not(argv[0] == 'om' or argv[0] == 'ups'):
        raise Exception("Sorry, first argument must be 'om' or 'ups' to "
                        "specify the physical quantity of interest.")
    elif len(argv) < 1:
        raise Exception("Insufficient number of arguments.")
    else:
        typ = argv[0]
        # could get rid of the conditional statement here, but too lazy atm
        if not(os.path.isfile('dbin')):
            with open('dbin', 'w') as file:
                file.write(' &BURG C=2.d0 &END')
        if typ == 'om':
            files = glob.glob('om-*')
            for i in files:
                name = i.split('.')[0]
                sp.check_call(['ln', '-sf', i, 'xout'])
                sp.check_call('burg.x')
                sp.check_call(['mv', 'xbout', name + '.burg'])
        else:
            files = glob.glob('ups-*')
            for i in files:
                name = i.split('.')[0]
                sp.check_call(['ln', '-sf', i, 'xout'])
                sp.check_call('burg.x')
                sp.check_call(['mv', 'xbout', name + '.burg'])


if __name__ == '__main__':
    main(sys.argv[1:])
