#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:29:08 2024

@author: georgios
"""

import numpy as np
import random
import math


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

    n_communities = 4
    n_points = 100

    data_ascii_txt = dataFolder + 'data' + '_n' + str(n_points) + '_c' + str(n_communities) + '_s' + str(seed1) + '.txt'
    png_file = dataFolder + 'clusters' + '_n' + str(n_points) + '_c' + str(n_communities) + '_s' + str(seed1) + '.png'
    
    
    
    pos = np.loadtxt(data_ascii_txt)
    
    # color the nodes according to their partition
    #cmap = cm.get_cmap('viridis', nComms + 1)
    clr = ['c','b','m','g','y','r']
    color_list = [ clr[int(x)] for x in pos[:,2] ]
    
    font = {'size' :10}
    matplotlib.rc('font', **font)
    #rcParams.update({'figure.autolayout': True})
    fac1=5
    degree = 10
    plt.figure(figsize=(6,6))
    #fig, ax = plt.subplots(2,1, sharey=False, gridspec_kw={'hspace': 0.2}, figsize=(4,6))
    jet = plt.get_cmap('jet')

    blobs_list = set(list(pos[:,2]))
    for i in range(len(pos)):
        plt.plot(pos[i,0],pos[i,1],'s', color=color_list[i] )
        
    plt.savefig(png_file,dpi=400) # save as png
