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

    # prepare output and append initial state
    output.initialize(t, x, t_max)

    while t < t_max:
        # find reaction hazards
        hazards = k * (x ** reactants).prod(axis=1)

        # cumulative distribution
        cdv = np.cumsum(hazards)
        # total hazard
        h0 = cdv[-1]
        cdv /= h0

        # sample reaction index
        index = sample_discrete(cdv)

        # sample exponential time
        delta_t = - 1.0 / h0 * np.log(np.random.uniform())

        # update state
        t = t + delta_t
        x = x + reaction_matrix[index]

        # append to output
        output.append(t, x)

    # transform to ndarrays
    ts, xs = output.as_ndarrays()

    return ts, xs
