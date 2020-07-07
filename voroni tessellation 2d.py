# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 01:03:53 2020

@author: carra
"""

import numpy as np
import matplotlib.pyplot as plt
points = np.random.rand(10,2)
from scipy.spatial import Voronoi, voronoi_plot_2d
vor = Voronoi(points)
fig = voronoi_plot_2d(vor)
fig = voronoi_plot_2d(vor,show_verticies=False,line_color='blue',line_width=2, line_alpha=0.6,point_size=3)
plt.show()
