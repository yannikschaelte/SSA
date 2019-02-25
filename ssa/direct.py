import numba as nb
import numpy as np

from .util import sample_discrete
from .output import Output


#@nb.jit
def direct(
        reactants: np.ndarray,
        reaction_matrix: np.ndarray,
        x0: np.ndarray,
        k: np.ndarray,
        t_max: np.ndarray,
        output: Output):
    # prepared running variables
    t = 0.0
    x = x0.copy()

    # prepare output
    output.initialize(t_max=t_max)

    # append initial state
    output.append(t, x)

    while t < t_max:
        # find reaction hazards
        hazards = k * (x ** reactants).prod(axis=1)
        h0 = np.sum(hazards)

        # sample reaction index
        index = sample_discrete(hazards / h0)

        # sample time
        delta_t = np.random.exponential(scale = 1.0 / h0)

        # update state
        t = t + delta_t
        x = x + reaction_matrix[index]

        # update trajectory
        output.append(t, x)

    # tidy up output
    output.finalize()

    # transform to ndarrays
    ts, xs = output.as_ndarrays()

    return ts, xs
