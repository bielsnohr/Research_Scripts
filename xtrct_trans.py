#!/usr/bin/env python
'''
@name: /Users/Matt/Google Drive/Python_workspace/Research_Scripts/xtrct_trans.py
@author: Matt
@date: Mar 25, 2014
@version: 1
@description: A python module/script for extracting multiple transitions from
    either an OMEGA or adf04 type 3 file with a consistent naming of the
    subsequent files containing the transition data.
'''
import sys
import subprocess as sp
import os
import datetime as dt


def main(argv):
    '''
    Main function for the xtrct_trans.py module
    Input/Usage: [om, ups] [source_calculation_descrip] [pairs of numbers
    representing the levels for the desired transitions]
    '''
    AS = True
    if not(argv[0] == 'om' or argv[0] == 'ups'):
        raise Exception("Sorry, first argument must be 'om' or 'ups' to "
                        "specify the physical quantity of interest.")
    elif len(argv) < 4:
        raise Exception("Insufficient number of arguments.")
    else:
        typ = argv[0]
        desc = argv[1]
        x = argv[2:]
        if len(x) % 2 is not 0:
            raise Exception("You have given an odd number of levels numbers."
                            " This needs to be even silly.")
        trans = [x[(2 * i): (2 * i + 2)] for i in range(int(len(x) / 2))]
        print(trans)
        if typ == 'om' and not(AS):
            if not(os.path.isfile('OMEGA')) and not(os.path.isfile('OMEGAU')):
                raise Exception('No OMEGA/U file in current directory.')
            for i in trans:
                try:
                    [int(a) for a in i]
                except ValueError as err:
                    # TO-DO: implement a float conversion here
                    print("You must enter integers for levels.")
                    print("You entered: ", err.args)
                    raise
                with open('tmp', 'w') as file:
                    file.write(i[0] + ' -' + i[1])
                sp.check_call('xtrct.x < tmp', shell=True)
                sp.check_call(['mv', 'xout', 'om-' + i[0] + '_' + i[1] + '-' +\
                               desc + '-' + dt.date.today().isoformat().\
                               replace('-', '_') + '.trns'])
                print("Done transition ", i[0], ' --> ', i[1])
                print("-------------------")
        else:
            if os.path.isfile('adf04') == False:
                raise Exception('No adf04 file in current directory.')
            for i in trans:
                try:
                    [int(a) for a in i]
                except ValueError as err:
                    # TO-DO: implement a float conversion here
                    print("You must enter integers for levels.")
                    print("You entered: ", err.args)
                    raise
                with open('tmp', 'w') as file:
                    file.write(i[0] + ' ' + i[1])
                if AS:
                    sp.check_call('xtrct_adf04.x < tmp', shell=True)
                    #T0-DO: make a function for the file name formatting
                    if typ == 'ups':
                        sp.check_call(['mv', 'x4out', 'ups-' + i[0] + '_' + i[1] +\
                                       '-' + desc + '-' + dt.date.today().isoformat().\
                                       replace('-', '_') + '.trns'])
                    else:
                        sp.check_call(['mv', 'x4out', 'om-' + i[0] + '_' + i[1] +\
                                       '-' + desc + '-' + dt.date.today().isoformat().\
                                       replace('-', '_') + '.trns'])
                else:
                    sp.check_call('xtrctups.x < tmp', shell=True)
                    sp.check_call(['mv', 'upsout', 'ups-' + i[0] + '_' + i[1] +\
                                   '-' + desc + '-' + dt.date.today().isoformat().\
                                   replace('-', '_') + '.trns'])
                print("Done transition ", i[0], ' --> ', i[1])
                print("-------------------")

if __name__ == '__main__':
    main(sys.argv[1:])
