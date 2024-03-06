#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:23:36 2024

@author: georgios
"""

import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc
from matplotlib import rcParams


if __name__ == '__main__':

    mainFolder = '/Users/georgios/MyStuff/MyCode/'

    dataFolder = mainFolder + 'spatialCommunities/'
    print('dataFolder=', dataFolder, flush=True )
    seed1 = 3
    print('seed1 =',seed1)

    n_blobs = 4
    n_points = 100

    png_file = dataFolder + 'clusComms' + '_n' + str(n_points) + '_c' + str(n_blobs) + '_s' + str(seed1) + '.png'

    in_data_ascii_txt1 = dataFolder + 'data' + '_n' + str(n_points) + '_c' + str(n_blobs) + '_s' + str(seed1) + '.txt'
    pos = np.loadtxt(in_data_ascii_txt1)

    in_data_ascii_txt3 = dataFolder + 'comms' + '_n' + str(n_points) + '_c' + str(n_blobs) + '_s' + str(seed1) + '.txt'
    Qs = np.loadtxt(in_data_ascii_txt3)
    Q = Qs[0]
    print('Q =', Q)
    Qstr = str(np.floor(Q*1000)/1000)
    nStr = str(len(Qs)-1)

    in_data_ascii_txt2 = dataFolder + 'comms2' + '_n' + str(n_points) + '_c' + str(n_blobs) + '_s' + str(seed1) + '.txt'
    Cs = np.loadtxt(in_data_ascii_txt2)
    nNodes2 = len(Cs)
    print('nNodes2 =', nNodes2)

    
    # color the nodes according to their partition
    #cmap = cm.get_cmap('viridis', nComms + 1)
    clr = ['c','b','m','g','r','y']
    color_list1 = [ clr[int(x)] for x in pos[:,2] ]
    color_list2 = [ clr[int(x)] for x in Cs[:,1] ]
    
    font = {'size' :10}
    matplotlib.rc('font', **font)
    #rcParams.update({'figure.autolayout': True})
    fac1=5
    degree = 10
    #plt.figure(figsize=(6,6))
    fig, ax = plt.subplots(2,1, sharey=False, gridspec_kw={'hspace': 0.2}, figsize=(4,6))
    jet = plt.get_cmap('jet')

    blobs_list = set(list(pos[:,2]))
    for i in range(len(pos)):
        ax[0].plot(pos[i,0],pos[i,1],'s', color=color_list1[i] )
        ax[1].plot(pos[i,0],pos[i,1],'s', color=color_list2[i] )
        
    
    ax[0].set(title='blobs, n= ' + str(n_blobs) )
    ax[1].set(title='communities, n= ' + nStr  + ', Q=' + Qstr)
    plt.savefig(png_file,dpi=400) # save as png


