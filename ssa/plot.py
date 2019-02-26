import matplotlib.pyplot as plt
import numpy as np
from typing import List

from .result import Result

def plot(
        result: Result,
        x_indices: List[int] = None,
        x_names: List[str] = None,
        show_mean: bool = False,
        show_std: bool = False,
        show: bool = False):
    # number of replicates
    n_reps = len(result.list_ts)

    # species to plot
    if x_indices is None:
        x_indices = list(range(result.list_xs[0][0, :].size))
    n_indices = len(x_indices)

    # labels
    if x_names is None:
        x_names = ["x" + str(ix) for ix in x_indices]

    # need a color
    cm = plt.get_cmap()

    # plot  
    fig, ax = plt.subplots()
    for ix in range(n_indices):
        for ir in range(n_reps):
            ax.step(result.list_ts[ir],
                    result.list_xs[ir][:, x_indices[ix]],
                    color=cm(ix / n_indices),
                    alpha = 0.5,
                    label=x_names[ix])
    
    # legend
    leg_lines = [plt.Line2D([0], [0], color=cm(ix / n_indices)) for ix in range(n_indices)]
    ax.legend(leg_lines, x_names)

    # show on screen
    if show:
        plt.show()
        return fig, ax
