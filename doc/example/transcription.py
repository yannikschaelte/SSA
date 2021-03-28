import ssa
import numpy as np
import matplotlib.pyplot as plt


def run():
    reactants = np.array([[0], [1]])
    products = np.array([[1], [0]])

    x_names = "mRNA"

    t_max = 1e2
    x0 = np.array([0])
    k = np.array([10, 0.1])

    model = ssa.Model(reactants=reactants, products=products, t_max=t_max, x0=x0, k=k)
    result = model.simulate(n_reps=10)
    ssa.plot(result)

    plt.savefig("transcription.png")


run()
