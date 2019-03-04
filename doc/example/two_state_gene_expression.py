import sys
sys.path.insert(0, '/home/yannik/ssa')

import ssa
import numpy as np


def run():
    reactants = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    products = np.array([[0, 1, 0, 0], [1, 0, 0, 0], [0, 1, 1, 0], [1, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]])

    k = np.array([10, 10, 0.5, 0.05, 10, 1, 0.2])
    x0 = np.array([1, 0, 0, 0])
    t_max = 30

    output = ssa.output.ArrayOutput(np.linspace(0, t_max, 1000))

    x_names = ["inactive promoter", "active promoeter", "mRNA", "protein"]

    model = ssa.Model(reactants=reactants, products=products, k=k, x0=x0, t_max=t_max, output=output)
    result = model.simulate(n_reps=100)
    ssa.plot(result, x_names=x_names, show=True)


run()
