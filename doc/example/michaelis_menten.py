import sys
sys.path.insert(0, '/home/yannik/ssa')

import ssa
import numpy as np
import matplotlib.pyplot as plt


def run():
    reactants = np.array([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0]])
    products = np.array([[0, 0, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1]])

    volume = 1e-15
    
    x0 = np.array([5e-7, 2e-7, 0, 0])
    x0 = ssa.util.molar_concentration_to_molecule_number(x0, volume=volume)

    k = np.array([1e6, 1e-4, 0.1])
    k = ssa.util.k_det_to_k_stoch(k, reactants=reactants, volume=volume)

    print(x0, k)

    t_max = 50

    model = ssa.Model(reactants=reactants, products=products,
                      x0=x0, k=k, t_max=t_max)
    result = model.simulate(n_reps=20)
    x_names = ["S", "E", "SE", "P"]
    ssa.plot(result, x_names=x_names, show=False)
    plt.savefig("michaelis_menten.png")

run()
