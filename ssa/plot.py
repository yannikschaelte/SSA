import matplotlib.pyplot as plt
import numpy as np
from typing import List

from .result import Result

def plot(
        self,
        result: Result,
        x_indices: List[int] = None
        x_names: List[str] = None,
        disp: bool = False):
    # number of replicates
    n_reps = len(result.list_ts)

    # species to plot
    if x_indices is None:
        x_indices = list(range(n_reps))
    n_indices = len(x_indices)

    # labels
    if x_names is None:
        x_names = ["x" + str(ix) for ix in x_indices]

    # need a color

    # plot
    fig, ax = plt.subplots()
    for ix in range(n_indices):
        for ir in range(n_reps):
            ax.step(result.list_ts[ir],
                    result.list_xs[ir][:, x_indices[ix]],
                    color=colors[ix],
                    label=x_names[ix])
    fig.legend()
    if disp:
        plt.show()
        return fig, ax
