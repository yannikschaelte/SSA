import ssa
import numpy as np
import matplotlib.pyplot as plt


def run():
    reactants = np.array([[1, 1, 0], [0, 1, 0]])
    products = np.array([[0, 2, 0], [0, 0, 1]])
    x0 = np.array([299, 1, 0])
    t_max = 1.0
    k = np.array([0.3, 5])
    x_names = ["Susceptible", "Infected", "Recovered"]
    model = ssa.Model(reactants, products, x0=x0, t_max=t_max, k=k)
    result = model.simulate(n_reps=20)
    ssa.plot(result, x_names=x_names, set_xlim_to_t_max=False, show=False)
    plt.savefig("sir.png")


run()
