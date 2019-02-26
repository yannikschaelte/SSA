import sys
sys.path.insert(0, "/home/yannik/ssa")
import numpy as np
import matplotlib.pyplot as plt
import timeit
import cProfile
import scipy as sp

import ssa

def h(x, pre, c):
    return (x**pre).prod(1) * c

def gillespie(x, c, pre, post, max_t):
    """
    Gillespie simulation

    Parameters
    ----------

    x: 1D array of size n_species
        The initial numbers.

    c: 1D array of size n_reactions
        The reaction rates.

    pre: array of size n_reactions x n_species
        What is to be consumed.

    post: array of size n_reactions x n_species
        What is to be produced

    max_t: int
        Timulate up to time max_t

    Returns
    -------
    t, X: 1d array, 2d array
        t: The time points.
        X: The history of the species.
           ``X.shape == (t.size, x.size)``

    """
    t = 0
    t_store = [t]
    x_store = [x.copy()]
    S = post - pre

    while t < max_t:
        h_vec = h(x, pre, c)
        h0 = h_vec.sum()
        if h0 == 0:
            break
        delta_t = sp.random.exponential(1 / h0)
        # no reaction can occur any more
        if not sp.isfinite(delta_t):
            t_store.append(max_t)
            x_store.append(x)
            break
        reaction = sp.random.choice(c.size, p=h_vec/h0)
        t = t + delta_t
        x = x + S[reaction]

        t_store.append(t)
        x_store.append(x)

    return sp.asarray(t_store), sp.asarray(x_store)

def viz_y(result):
    _, ax = plt.subplots()
    nr = len(result.list_ts)
    for j in range(nr):
        ax.step(result.list_ts[j], result.list_xs[j][:, 0], color='b')
        ax.step(result.list_ts[j], result.list_xs[j][:, 1], color='r')

    plt.show()


reactants = np.array([[0, 0], [1, 0], [1, 0], [0, 1]])
products = np.array([[1, 0], [1, 1], [0, 0], [0, 0]])
x0 = np.array([0, 0])

k = np.array([1.0, 1.0, 0.1, 0.04])
t_max = 2e2
timepoints = np.linspace(0, t_max, 20)

def run():
    model = ssa.Model(reactants, products, x0, t_max, k, output = ssa.output.FullOutput())
    #model = ssa.Model(reactants, products, x0, t_max, k, output = ssa.output.ArrayOutput(timepoints))
    result = model.simulate(n_reps = 10)

    for j in range(len(result.list_ts)):
        #print(result.list_ts[j][-10:])
        #print(result.list_xs[j][-10:])
        pass

    #viz_y(result)

def run_gillespie():
    for _ in range(10):
        gillespie(x0, k, reactants, products, t_max)   

#cProfile.run("run()", 'restats')
#p.strip_dirs().sort_stats(-1).print_stats()
print(timeit.timeit("run()", setup="from __main__ import run", number=10))
print(timeit.timeit("run_gillespie()", setup="from __main__ import run_gillespie", number=10))
#viz_y(result.list_ts, result.list_xs)
