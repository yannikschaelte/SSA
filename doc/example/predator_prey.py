import ssa
import numpy as np
import matplotlib.pyplot as plt


def run():
    reactants = np.array([[1, 0], [1, 1], [0, 1]])
    products = np.array([[2, 0], [0, 2], [0, 0]])

    x0 = np.array([50, 100])
    k = np.array([1, 0.005, 0.6])
    t_max = 30
    output = ssa.output.FullOutput()

    model = ssa.Model(
        reactants, products, x0=x0, k=k, t_max=t_max, output=output, n_procs=2
    )
    result = model.simulate(n_reps=10)
    ssa.plot(result, show=False)
    plt.savefig("ex4.png")


run()
