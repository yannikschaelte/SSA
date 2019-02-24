import sys
sys.path.insert(0, "/home/yannik/ssa")
import numpy as np
import matplotlib.pyplot as plt

import ssa

reactants = np.array([[0, 0], [1, 0], [1, 0], [0, 1]])
products = np.array([[1, 0], [1, 1], [0, 0], [0, 0]])
x0 = np.array([0, 0])

k = np.array([1.0, 1.0, 0.1, 0.04])
t_max = 2e2


model = ssa.Model(reactants, products, x0, t_max, k, output = ssa.output.FullOutput())

result = model.simulate(n_reps = 10)

print(result.list_ts[0], result.list_xs[0])



def viz_y(ts, xs):
    _, ax = plt.subplots()
    nr = len(result.list_ts)
    for j in range(nr):
        ax.step(result.list_ts[j], result.list_xs[j][:, 0], color='b')
        ax.step(result.list_ts[j], result.list_xs[j][:, 1], color='r')

    plt.show()


viz_y(result.list_ts, result.list_xs)
