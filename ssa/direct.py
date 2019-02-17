import numba as nb
import numpy as np

from .util import sample_discrete


@nb.jit(nopython=True, nogil=True, cache=False)
def direct(
        reactants: np.ndarray,
        products: np.ndarray,
        x0: np.ndarray,
        k_stoch: np.ndarray,
        t_max: np.ndarray):
    """

    Parameters
    ----------
    """
    # compute reaction matrix
    reaction_matrix = products - reactants

    # prepared running variables
    t = 0
    x = x0.copy()

    # prepare output
    ts = [t]
    xs = [x]

    while t < t_max:
        # find reaction hazards
        hazards = k_stoch * (xt ** reactants).prod(axis=1)
        h0 = np.sum(hazards)

        # sample reaction index
        index = sample_discrete(hazards / h0)

        # sample time
        delta_t = np.random.exponential(scale = 1 / h0)

        # update state
        t = t + delta_t
        x = x + reaction_matrix[index]

        # update trajectory
        if t <= t_max:
            ts.append(t)
            xs.append(x)

    # transform to ndarrays
    ts = np.array(ts)
    xs = np.array(xs)

    return ts, xs
