#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:00:27 2024

@author: georgios
"""

import numpy as np

import networkx as nx
import networkx.algorithms.community as nxcom



if __name__ == '__main__':

    mainFolder = '/Users/georgios/MyStuff/MyCode/'

    dataFolder = mainFolder + 'spatialCommunities/'
    print('dataFolder=', dataFolder, flush=True )
    seed1 = 3
    print('seed1 =',seed1)

    n_blobs = 4
    n_points = 100

    in_data_ascii_txt = dataFolder + 'drs' + '_n' + str(n_points) + '_c' + str(n_blobs) + '_s' + str(seed1) + '.txt'
    out_data_ascii_txt1 = dataFolder + 'comms' + '_n' + str(n_points) + '_c' + str(n_blobs) + '_s' + str(seed1) + '.txt'
    out_data_ascii_txt2 = dataFolder + 'comms2' + '_n' + str(n_points) + '_c' + str(n_blobs) + '_s' + str(seed1) + '.txt'
    
    
    edge_list = np.loadtxt(in_data_ascii_txt)

    A = np.zeros([n_points,n_points])
    for item in edge_list:
        i = int(item[0])
        j = int(item[1])
        value = item[2]
        A[i,j] = value
        
    G = nx.Graph()
    G = nx.from_numpy_matrix(A)


    partition1 = nxcom.louvain_communities(G, seed=seed1)
    modularity2 = nxcom.modularity(G, partition1, weight='weight')
    print("The modularity Q based on louvain partition is {}".format(modularity2))   

    parts_lens = list()
    partition1.sort(key=len,reverse=True)
    for ipart in partition1:
        parts_lens.append(len(ipart))
    
    print('partitions size =',parts_lens)

    data1 = np.array([modularity2])
    data1 = np.r_[data1, np.asarray(parts_lens).T ]

    np.savetxt(out_data_ascii_txt1,data1,delimiter=' ')



    ii = -111
    parts_list = list()
    data2 = ii*np.ones(shape=[1,2])
    ii = -1
    for ipart in partition1:
        ii += 1
        iplist = list()
        iplist = list(ipart)
        iplist = sorted([int(x) for x in iplist])
        #parts_list.append(iplist)

        iparray0 = np.asarray(iplist)
        iparray1 = np.ones_like(iparray0)
    
        iparray01 = np.c_[iparray0,ii*iparray1]
    
        data2 = np.r_[data2,iparray01]
        print('np.shape(data2)=', np.shape(data2))
    
    data2 = np.delete(data2, (0), axis=0)
    print('np.shape(data2)=', np.shape(data2))

    data2 = data2[data2[:, 0].argsort()]

    np.savetxt(out_data_ascii_txt2,data2,fmt='%i',delimiter=' ')
