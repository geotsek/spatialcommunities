In this repo I have put together python code for spatial community detection.

How it works:
(0. I create some random points in space that form blobs to test/run the main algorithm below. This step is not needed when one has their own data points.)
1. From a collection of points in cartesian coordinates (eg cells in a field of view on a slide, or anything) the code first will create an all-to-all network encoding the spatial information. In the network the points are the nodes, and the links between 2 nodes are given a weight equal to the inverse of the distance between these nodes/points. In that way nodes/points that are close have strong weights/connections. This is a slow O(N^2) operation where all pairs of N nodes have their distance calculated, but it only needs to be calculated once.
2. On the constructed network, I then apply a community detection algorithm. I use the well-known Louvain algorithm in its networkx implementation. The algorithm will find a community structure by minimizing the modularity Q of the weighted network, i.e. it will try to maximize the connectivity between intra-community nodes and minimize the connectivity between inter-community nodes. The algorithm is very fast (very likely still the fastest out there) but it does not guarantee to find the best community structure. As a consequence it needs to be run a few times and rely on the most robust/repeated results.


