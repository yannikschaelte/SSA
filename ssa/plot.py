import matplotlib.pyplot as plt
import numpy as np
from typing import List, Union

from .result import FullResult, ArrayResult


def plot(
        result: Union[FullResult, ArrayResult],
        x_indices: List[int] = None,
        x_names: List[str] = None,
        show_mean: bool = False,
        show_std: bool = False,
        show: bool = False):
    # generate matrix
    if isinstance(result, FullResult):
        result = result.for_timepoints()

    # dimensions
    nr, nt, nx = result.matrix_xs.shape
    print(nr, nt, nx)
    # species to plot
    if x_indices is None:
        x_indices = list(range(nx))
    n_indices = len(x_indices)

    # labels
    if x_names is None:
        x_names = ["x" + str(ix) for ix in x_indices]

    # need a color
    cm = plt.get_cmap()

    # plot  
    fig, ax = plt.subplots()
    for ix in range(n_indices):
        for ir in range(nr):
            ax.step(result.ts,
                    result.matrix_xs[ir, :, x_indices[ix]],
                    color=cm(ix / n_indices),
                    alpha=0.5,
                    label=x_names[ix])
    
    # legend
    leg_lines = [plt.Line2D([0], [0], color=cm(ix / n_indices)) for ix in range(n_indices)]
    ax.legend(leg_lines, x_names)

    # mean
    mean = np.mean(result.matrix_xs, axis=0)
    if show_mean:
        ax.step(result.ts, mean, alpha = 1.0, label="mean")

    # show on screen
    if show:
        plt.show()
        return fig, ax

