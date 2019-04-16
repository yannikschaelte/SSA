import sys
sys.path.insert(0, '/home/yannik/ssa')

import ssa
import numpy as np
import matplotlib.pyplot as plt


def run():
    reactants = np.array([[0], [1]])
    products = np.array([[1], [0]])

    t_max = 120
    x0 = np.array([0])
    k = np.array([1, 0.05])

    output = ssa.output.ArrayOutput(np.linspace(0, t_max, 100))
    output = ssa.output.FullOutput()

    model = ssa.Model(reactants=reactants, products=products, t_max=t_max, x0=x0, k=k, output=output)
    result = model.simulate(n_reps=10)

    x_names = ["mRNA"]
    ssa.plot(result, show=False, x_names=x_names)
    plt.savefig("mrna_transcription.png")


run()
