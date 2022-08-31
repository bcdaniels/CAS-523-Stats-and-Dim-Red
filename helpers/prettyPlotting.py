# prettyPlotting.py
#
# Bryan Daniels
# 2022/8/31
#
# Gathering code for producing some useful and nice-looking plots.
#

from matplotlib import pyplot as plt
import numpy as np

def scatter1D(data,size=100,figsize=(10,0.5)):
    """
    Make a one-dimensional scatter plot.
    """
    plt.figure(figsize=figsize)
    plt.scatter(data,np.zeros_like(data),clip_on=False,s=size,zorder=3)
    plt.axis(ymin=0)
    plt.gca().get_yaxis().set_visible(False)
    for loc in ['left','right','top']: plt.gca().spines[loc].set_color('none')
