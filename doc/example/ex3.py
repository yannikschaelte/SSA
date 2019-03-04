import sys
sys.path.insert(0, '/home/yannik/ssa')

import ssa
import numpy as np
import matplotlib.pyplot as plt


def run():
    reactants0 = np.array([[1, 1]])
    products0 = np.array([[0, 2]])

    reactants1 = np.array([[1, 0]])
    products1 = np.array([[0, 1]])

    x0 = np.array([40, 3])
    t_max = 0.1
    
    k0 = np.array([2.3])
    k1 = np.array([30.0])

    nr = 5

    output = ssa.output.FullOutput()

    model0 = ssa.Model(reactants0, products0, x0, t_max, k0, output, n_procs=2)
    result0 = model0.simulate(n_reps=nr)
    _, axes = plt.subplots(1, 2)
    ssa.plot(result0, show=False, ax=axes[0])

    model1 = ssa.Model(reactants1, products1, x0, t_max, k1, output, n_procs=2)
    result1 = model1.simulate(n_reps=nr)
    ssa.plot(result1, show=False, ax=axes[1])

    plt.show()

run()
