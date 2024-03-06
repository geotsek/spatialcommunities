#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:29:19 2024

@author: georgios
"""

import numpy as np
from sklearn.datasets import make_blobs


if __name__ == '__main__':

    mainFolder = '/Users/georgios/MyStuff/MyCode/'

    dataFolder = mainFolder + 'spatialCommunities/'
    print('dataFolder=', dataFolder, flush=True )
    seed1 = 3
    print('seed1 =',seed1)

    n_blobs = 4
    n_points = 100

    out_data_ascii_txt = dataFolder + 'data' + '_n' + str(n_points) + '_c' + str(n_blobs) + '_s' + str(seed1) + '.txt'

    #centers = [(5,5), (-5,5), (-5,-5), (5,-5)]
    #centers = [(1.5,1.5), (-1.5,1.5), (-1.5,-1.5), (1.5,-1.5)]
    centers = [(1,1), (-1,1), (-1,-1), (1,-1)]
    #cluster_std = [1,0.8,1.2,1]
    cluster_std = [1,1.0,1.0,1.0]

    pos = make_blobs(n_samples=n_points, n_features=n_blobs, cluster_std=cluster_std, centers=centers , random_state=seed1)
    
    data = np.asarray(pos[0])
    data = np.c_[data,pos[1]]
    np.savetxt(out_data_ascii_txt,data,fmt='%.5f',delimiter=' ')




