import sys
sys.path.insert(0, '/home/yannik/ssa')

import ssa
import numpy as np


def run():
    reactants = np.array([[2, 0], [0, 1]])
    products = np.array([[0, 1], [2, 0]])

    volume=1e-15
    use_na=True

    k_det = np.array([5e5, 0.2])
    k1 = ssa.util.k_det_to_k_stoch(k_det, reactants=reactants, volume=volume, use_na=use_na)
    k2 = np.array([1.66e-3, 0.2])
    print(k1, k2)

    x0_molar_concentration = np.array([5e-7, 0])
    x01 = ssa.util.molar_concentration_to_molecule_number(x0_molar_concentration, volume=volume, use_na=use_na)
    x02 = np.array([301.1, 0])
    print(x01, x02)
    t_max = 10.0

    model = ssa.Model(reactants=reactants, products=products,
                      k=k2, x0=x02, t_max=t_max, n_procs=2)
    result = model.simulate(n_reps=5)
    ssa.plot(result, show=True)

run()
