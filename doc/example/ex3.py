import sys
sys.path.insert(0, '/home/yannik/ssa')

import ssa
import numpy as np


def run():
    reactants = np.array([[1, 1]])
    products = np.array([[0, 2]])
    x0 = np.array([40, 3])
    t_max = 0.1
    k = np.array([2.3])
    output = ssa.output.FullOutput()

    model = ssa.Model(reactants, products, x0, t_max, k, output, n_procs=2)
    result = model.simulate(n_reps=10)
    ssa.plot(result, show=True)

run()
