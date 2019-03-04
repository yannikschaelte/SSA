import sys
sys.path.insert(0, "/home/yannik/ssa")
import numpy as np
import timeit
import cProfile

import ssa


def run():
    reactants = np.array([[1, 0, 0], [0, 1, 0]])
    products = np.array([[0, 1, 0], [0, 0, 1]])
    x0 = np.array([100, 0, 0])

    k = np.array([1.0, 1.0])
    t_max = 10
    timepoints = np.linspace(0, t_max, 1000)

    model = ssa.Model(reactants, products, x0, t_max, k, output = ssa.output.FullOutput(), n_procs=2)
    #model = ssa.Model(reactants, products, x0, t_max, k, output = ssa.output.ArrayOutput(timepoints), n_procs=1)
    result = model.simulate(n_reps = 10)

    for j in range(len(result.list_ts)):
        pass
    ssa.plot(result, show=True, show_mean=True, show_std=True)



#cProfile.run("run()", 'restats')
#p.strip_dirs().sort_stats(-1).print_stats()
#print(timeit.timeit("run()", setup="from __main__ import run", number=10))
run()

#viz_y(result.list_ts, result.list_xs)
