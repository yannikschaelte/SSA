import sys
sys.path.insert(0, '/home/yannik/ssa')

import ssa
import numpy as np
import matplotlib.pyplot as plt


def run():
    reactants = np.array([[0, 0], [1, 0], [1, 0], [0, 1]])
    products = np.array([[1, 0], [0, 0], [1, 1], [0, 0]])

    t_max = 30
    x0 = np.array([0, 0])
    k = np.array([100, 1, 1, 0.4])

    output = ssa.output.ArrayOutput(np.linspace(0, t_max, 100))

    model = ssa.Model(reactants=reactants, products=products, t_max=t_max, x0=x0, k=k, output=output)
    result = model.simulate(n_reps=20)
    ssa.plot(result, show=False)
    plt.savefig("one_state_gene_expression.png")


run()
