import sys

sys.path.insert(0, "/home/yannik/ssa")

import ssa
import numpy as np
import matplotlib.pyplot as plt


def run():
    reactants = np.array([[0, 0], [1, 0], [0, 1]])
    products = np.array([[1, 0], [0, 1], [0, 0]])

    k = np.array([1.0, 0.1, 0.05])
    x0 = np.array([100, 0])
    t_max = 100

    model = ssa.Model(reactants=reactants, products=products, k=k, x0=x0, t_max=t_max)
    result = model.simulate(n_reps=20)
    ssa.plot(result, show=False)
    plt.savefig("mono_molecular_chain.png")


run()
