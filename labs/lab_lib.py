import numpy as np
import pandas as pd
# %matplotlib inline
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats
 
set_matplotlib_formats ('png')

def my_plot (x1, y1, xerr = 0, yerr = 0, title="", xlabel="", ylabel="", number=1):

    k1, s1 = np.polyfit (x1, y1, deg=1, cov=True)

    plt.figure()

    fig, ax1 = plt.subplots(figsize=(16, 16), dpi=100)

    ax1.set_title (title)

    ax1.set_ylabel (ylabel) 
    ax1.set_xlabel (xlabel)

    # ax1.scatter (x1, y1, marker=".", s = 100)

    plt.errorbar (x1, y1, yerr=yerr, xerr=xerr, fmt='o-', ecolor='red', ls='none')

    ax1.plot (x1, np.poly1d (k1)(x1))

    plt.savefig(f"./picturies/graph{number}.png", dpi=100)
    plt.grid()
    plt.show()