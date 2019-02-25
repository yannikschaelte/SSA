import numba as nb
import numpy as np


# Avogadro's constant, [mol**(-1)]
NA = 6.02214085774e23


#@nb.jit
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
def sample_discrete(propensities):
    """
    Sample an index from weighted discrete distribution.

    Parameters
    ----------

    propensities: np.ndarray, shape = (nr, )
        Propensity vector. The sum of weights is not requried to be normalized
        to 1.

    Returns
    -------

    index: int
        The index in [0, nr - 1] sampled according to the propensity weights.
    """
    # cumulative distribution function
    cdf = propensities.cumsum()
    # normalize to 1
    cdf /= cdf[-1]
    # sample
    p = np.random.uniform()
    # find right index of where p would be inserted
    index = cdf.searchsorted(p, side='right')

    return index
