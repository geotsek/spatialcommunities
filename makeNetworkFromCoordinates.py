#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:08:22 2024

@author: georgios
"""

import numpy as np


def getAllPairDistances(pos):
    
    n_points, n_dim = np.shape(pos)
    print('n_points=',n_points,'  n_dim=',n_dim)
        
    pos_x = pos[:,0]
    pos_y = pos[:,1]
    dx = pos_x[:,np.newaxis]-pos_x
    dy = pos_y[:,np.newaxis]-pos_y
    print('shape of dx before triu = ', np.shape(dx))

    idx = np.triu_indices(n_points,1)
    print('shape of idx = ', np.shape(idx))
    print('idx[0:10] = ', idx)


    dx = np.ndarray.flatten(dx[idx])
    dy = np.ndarray.flatten(dy[idx])
    #it keeps the N diag elements, with the N*(N-1)/2 off-diag elements so numPairs = N*(N+1)/2
    #removes the N diag elements (self-distance of dr=0.0) so only the N*(N-1)/2 off-diag elements remain
    print('shape of dx after flatten= ', np.shape(dx))
        
    
    dr_mag = np.sqrt(np.square(dx) + np.square(dy))
    #print('dr_mag =',dr_mag)
    
    '''
    dr_vec = np.vstack((dx, dy))
    #print('dr_vec =',dr_vec)
    
    dr_mag = np.linalg.norm(dr_vec,axis=0)
    #print('dr_mag =',dr_mag)
    '''
    
    (numPairs) = np.size(dr_mag)
    print('numPairs = ', numPairs)
    #print('dr_mag = ', dr_mag)
    print('max(dr_mag) = ', np.max(dr_mag) )
    print('min(dr_mag) = ', np.min(dr_mag) )
    print('shape of dr_mag = ', np.shape(dr_mag))
    
    return dr_mag, np.transpose(idx)
    
if __name__ == '__main__':

    mainFolder = '/Users/georgios/MyStuff/MyCode/'

    dataFolder = mainFolder + 'spatialCommunities/'
    print('dataFolder=', dataFolder, flush=True )
    seed1 = 3
    print('seed1 =',seed1)

    n_communities = 4
    n_points = 100

    in_data_ascii_txt = dataFolder + 'data' + '_n' + str(n_points) + '_c' + str(n_communities) + '_s' + str(seed1) + '.txt'
    out_data_ascii_txt = dataFolder + 'drs' + '_n' + str(n_points) + '_c' + str(n_communities) + '_s' + str(seed1) + '.txt'
    
    
    coords = np.loadtxt(in_data_ascii_txt)
    
    pos = coords[:,0:2]
    
    drs, idx = getAllPairDistances(pos)
    
    weights = 1/drs
    
    data = np.c_[idx,weights]
    
    np.savetxt(out_data_ascii_txt,data,fmt='%.5f',delimiter=' ')

    