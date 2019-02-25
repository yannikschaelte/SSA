import numba as nb
import numpy as np


# Avogadro's constant, [mol**(-1)]
NA = 6.02214085774e23


def get_k_stoch(
        k_det: np.ndarray,
        reactants: np.ndarray,
        volume: float,
        use_na: bool):
    nr = reactants.shape[0]

    reaction_orders = np.sum(reactants, axis=1)
    if reaction_orders.max() > 2:
        raise ValueError(
            "Generation of stochastic reaction coefficient constants "
            "from reactions of order > 2 currently not supported. "
            "Consider rewriting in terms of simpler reactions.")
    
    k_stoch = k_det.copy()
    
    if use_na:
        factor = NA * volume
    else:
        factor = 1.0 * volume

    for ir in range(nr):
        k_stoch[ir] /= np.power(factor, reaction_orders[ir] - 1)
        if np.max(reactants[ir, :]) == 2:
            k_stoch[ir] *= 2

    return k_stoch


#@nb.jit
def sample_discrete(cdv):
    """
    Sample an index from a weighted discrete distribution.

    Parameters
    ----------

    cdv: np.ndarray, shape = (nr, )
        Cumulative distribution vector associated with the propensity
        vector.

    Returns
    -------

    index: int
        The index in [0, nr - 1] sampled according to the propensity weights.
    """
    # sample
    p = np.random.uniform()
    # find right index of where p would be inserted
    index = cdv.searchsorted(p, side='right')

    return index
