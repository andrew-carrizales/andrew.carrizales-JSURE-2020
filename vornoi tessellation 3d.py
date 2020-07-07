# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 01:03:52 2020

@author: carra
"""

import scipy.spatial
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from matplotlib import colors
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

#calculate points in single hemisphere
phi = np.linspace(0,2*np.pi,10,endpoint=False) #azimuth angle
theta = np.linspace(0.001,np.pi*0.4,5) #polar angle
theta = theta[np.newaxis,:].T
radius = 1;
phiv,thetav = np.meshgrid(phi, theta)
phiv = np.reshape(phiv,(50,1))
thetav = np.reshape(thetav,(50,1))


x = radius*np.cos(phiv)*np.sin(thetav)
y = radius*np.sin(phiv)*np.sin(thetav)
z = radius*np.cos(thetav)


points = np.concatenate([x,y,z],axis=1)
#Voronoi-Regions
sv = scipy.spatial.SphericalVoronoi(points)
sv.sort_vertices_of_regions()


#plotting
fig = plt.figure()
ax = fig.add_subplot('111', projection='3d')
ax.scatter(points[...,0], points[...,1], points[...,2])
for region in sv.regions:
    random_color = colors.rgb2hex(np.random.rand(3))
    polygon = Poly3DCollection([sv.vertices[region]], alpha=1.0)
    polygon.set_color(random_color)
    ax.add_collection3d(polygon)
    
ax.set_xlim([-1.0,1.0])
ax.set_ylim([-1.0,1.0])
ax.set_zlim([-1.0,1.0])
ax.view_init(45,0)

fig.savefig('hemisphere.png', dpi=300)


     
     
