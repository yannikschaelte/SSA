import sys
sys.path.insert(0, "/home/yannik/ssa")
import numpy as np
import matplotlib.pyplot as plt
import timeit
import cProfile

import ssa

def viz_y(result):
    _, ax = plt.subplots()
    nr = len(result.list_ts)
    for j in range(nr):
        ax.step(result.list_ts[j], result.list_xs[j][:, 0], color='b')
        ax.step(result.list_ts[j], result.list_xs[j][:, 1], color='r')

    plt.show()

def run():
    reactants = np.array([[0, 0], [1, 0], [1, 0], [0, 1]])
    products = np.array([[1, 0], [1, 1], [0, 0], [0, 0]])
    x0 = np.array([0, 0])

    k = np.array([1.0, 1.0, 0.1, 0.04])
    t_max = 2e2
    timepoints = np.linspace(0, t_max, 20)

    model = ssa.Model(reactants, products, x0, t_max, k, output = ssa.output.FullOutput(), n_procs=2)
    #model = ssa.Model(reactants, products, x0, t_max, k, output = ssa.output.ArrayOutput(timepoints), n_procs=2)
    result = model.simulate(n_reps = 100)

    for j in range(len(result.list_ts)):
        #print(result.list_ts[j][-10:])
        #print(result.list_xs[j][-10:])
        pass
    ssa.plot(result, show=True)
    #viz_y(result)



#cProfile.run("run()", 'restats')
#p.strip_dirs().sort_stats(-1).print_stats()
#print(timeit.timeit("run()", setup="from __main__ import run", number=10))
run()

#viz_y(result.list_ts, result.list_xs)
