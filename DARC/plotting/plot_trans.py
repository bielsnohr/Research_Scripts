#!/usr/bin/env python
'''
@name: plot_trans.py
@author: Matt
@date: 2014-04-30
@version: 1.0
@description: A python script for plotting the (effective) collision strengths
    for transitions from different calculations on the same graph. All data
    relevant files will be plotted for a specified transition and multiple
    transitions can be specified. The file names must be formatted exactly as
    those produced from the xtrct_trans.py module.
'''

import numpy as np
import matplotlib.pyplot as plt
import sys
import math
#import subprocess as sp
#import os
import datetime as dt
import glob



def main(argv):
    '''Main function for module plot_trans
    Input: plot_trans.py [om,ups] ["list of transitions specified by pairs of
    numbers, lower level then upper level"] { -s [description]}
    '''
    # Level nomenclature
    lev = {'1':'3d^{10}\!4s^2 \ ^1\!S_0^{\circ}', '275':\
            '3d^{9}\!4s^2\!4f \ \ ^3\!D_1^{\circ}', '290':\
            '3d^{9}\!4s^2\!4f \ \ ^1\!P_1^{\circ}', '295':\
            '3d^{9}\!4s^2\!4f \ \ ^3\!P_1^{\circ}'}
    LOGY = False
    LOGX = True
    if not(argv[0] == 'om' or argv[0] == 'ups'):
        raise Exception("Sorry, first argument must be 'om' or 'ups' to "
                        "specify the physical quantity of interest.")
    elif len(argv) < 3:
        raise Exception("Insufficient number of arguments.")
    elif argv[1] == '-s':
        raise Exception("You need to specify at least one transition.")
    else:
        typ = argv[0]
        if argv[-2] == '-s':
            save = True
            outfile = argv[-1]
            x = argv[1:-2]
        else:
            save = False
            x = argv[1:]
        if len(x) % 2 is not 0:
            raise Exception("You have given an odd number of levels."
                            " This needs to be even silly.")
        trans = [x[(2 * i): (2 * i + 2)] for i in range(int(len(x) / 2))]
        print(trans)
        fname = []
        if typ == 'ups':
            for i in trans:
                try:
                    [int(a) for a in i]
                except ValueError as err:
                    # TO-DO: implement a float conversion here
                    print("You must enter integers for levels.")
                    print("You entered: ", err.args)
                    raise
                files = glob.glob('ups-' + i[0] + '_' + i[1] + '*')
                print(files)
                fig, ax = plt.subplots(1)
                legend = []
                title = 'Transition ' + i[0] + '-' + i[1] + ', $' + lev[i[0]]\
                        + '\\rightarrow' + lev[i[1]] + '$'
                fname.append('ups-' + i[0] + '_' + i[1] + '-' + outfile + '-'\
                             + dt.date.today().isoformat().replace('-', '_') +\
                             '.pdf')
                if LOGX:
                    maxx = 0
                    minx = 1e20
                if LOGY:
                    maxy = 0
                    miny = 1e20
                count = 1
                sty = ['-', '--', '-.', '-x', '-*']
                for j in files:
                    desc = j.split('-')[2]
                    legend.append(desc)
                    # Load the input files and plot the appropriate columns
                    data = np.loadtxt(j)
                    if desc == 'AS_DW':
                        x1 = data[0:-1, 0]
                    else:
                        x1 = data[0:-1, 1]
                    y1 = data[0:-1, 3]
                    if LOGX:
                        maxx = max(maxx, np.max(x1))
                        minx = min(minx, np.min(x1))
                    if LOGY:
                        maxy = max(maxy, np.max(y1))
                        miny = min(miny, np.min(y1))
                    ## Create the desired uncertainty region
                    #err = 0.1 * y2
                    ax.plot(x1, y1, sty[count - 1])
                    if count % 5 == 0:
                        count = 1
                    else:
                        count += 1
                    #ax.fill_between(x2, y2 - err, y2 + err, alpha=0.2, edgecolor='red', 
                    #        facecolor='red')
                if LOGX:
                    ax.set_xscale('log')
                    xmax = maxx + 10 ** math.floor(math.log10(maxx))
                    xmin = minx - 10 ** math.floor(math.log10(minx))
                    ax.set_xlim([xmin, xmax])
                if LOGY:
                    ax.set_yscale('log')
                    ymax = maxy + 10 ** math.floor(math.log10(maxy))
                    ymin = miny - 10 ** math.floor(math.log10(miny))
                    ax.set_ylim([ymin, ymax])
                ax.set_ylabel("$\\Upsilon$, Effective Collision Strength")
                ax.set_xlabel("$T \ (\mathrm{K})$")
                ax.set_title(title)
                ax.legend(legend, loc='upper left', prop={'size':10})
                fig.set_size_inches(11.89, 8.27)
            if save:
                for i in plt.get_fignums():
                    plt.figure(i)
                    plt.savefig(fname[i - 1])
            else:
                plt.show()
        else:
            pass

    # old code
    #if len(argv) < 3:
    #    raise Exception("Insufficient number of arguments")
    #print(argv, len(argv))
    #infile1 = argv[0]
    #infile2 = argv[1]
    ##title = argv[2]
    #lev1 = argv[2]
    #lev2 = argv[3]
    #save = False
    #if len(argv) == 6:  
    #    if argv[4] == '-s':
    #        save = True
    #        outfile = argv[5]

    #lev = {'1':'3d^{10}\!4s^2 \ ^1\!S_0^{\circ}', '275':\
    #        '3d^{9}\!4s^2\!4f \ \ ^3\!D_1^{\circ}', '290':\
    #        '3d^{9}\!4s^2\!4f \ \ ^1\!P_1^{\circ}', '295':\
    #        '3d^{9}\!4s^2\!4f \ \ ^3\!P_1^{\circ}'}
    #title = 'Transition ' + lev1 + '-' + lev2 + ', $' + lev[lev1] +\
    #        '\\rightarrow' + lev[lev2] + '$'
    ## Load the input files and plot the appropriate columns
    #data1 = np.loadtxt(infile1)
    #data2 = np.loadtxt(infile2)
    ##x2 = np.log10(data2[0:-2, 1])
    #x1 = data1[0:-2, 0]
    #y1 = data1[0:-2, 1]
    #x2 = data2[0:-2, 0]
    #y2 = data2[0:-2, 1]
    ## Create the desired uncertainty region
    #err = 0.1 * y2
    #fig, ax = plt.subplots(1)
    #ax.plot(x1, y1, 'b--') 
    #ax.plot(x2, y2, 'r-') 
    #ax.fill_between(x2, y2 - err, y2 + err, alpha=0.2, edgecolor='red', 
    #        facecolor='red')
    #ax.set_xscale('log')
    #ax.set_ylabel("$\\Upsilon$, Effective Collision Strength")
    #ax.set_xlabel("$T \ (\mathrm{K})$")
    #ax.set_title(title)
    #ax.legend(('W+44 AS DW MENGI=-1', 'W+44 AS DW MENGI=-2'), loc='upper left', prop={'size':10})
    #if save:
    #    plt.savefig(outfile)
    #else:
    #    plt.show()

if __name__ == '__main__':
    main(sys.argv[1:])
