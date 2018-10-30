# numpy
# Comparison of shapes

# D2 shape distribution

import numpy as np
import trimesh

filename = r'C:\Users\chlock\Documents\shapes\brackets\Bracket2_0.stl'

mesh = trimesh.load(filename)

# print(mesh.show())

# Gets all of the triangles in the stl
T = mesh.triangles
# print(T.shape)

each_triangle_area = np.array([np.linalg.norm(np.cross(t[1]-t[0], t[2]-t[0]))*0.5 for t in T])

# print(each_triangle_area)

# Assigning index to each triangle
triangle_indices = np.arange(len(each_triangle_area))

# Randomly sampling 1024 traingles based on the area
S = 1024
triangle_indices_sampled = np.random.choice(
    triangle_indices, S, replace=True,
    p=each_triangle_area/np.sum(each_triangle_area)
)

# print(triangle_indices_sampled)

sampled_triangles = T[triangle_indices_sampled]

r1 = np.random.uniform()

r2 = np.random.uniform()

Px = (1-np.sqrt(r1))*sampled_triangles[:,0]
Py = np.sqrt(r1)*(1-r2)*sampled_triangles[:,1]
Pz = np.sqrt(r1)*r2*sampled_triangles[:,2]

P = Px + Py + Pz

from itertools import combinations
D2_points = combinations(P, 2)

# print(D2_points)

distances = np.array([np.linalg.norm(pair[1]-pair[0]) for pair in D2_points])

import matplotlib.pyplot as plt

a = np.histogram(distances, bins = 1024)

plt.hist(distances, bins = 1024, histtype='step')
plt.show()
