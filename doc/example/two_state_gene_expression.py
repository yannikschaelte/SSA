import ssa
import numpy as np
import matplotlib.pyplot as plt


def run():
    # activation, deactivation, transcription-act,
    #  transcription-deact, translation, mRNA decay,
    #  protein decay
    reactants = np.array(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )
    products = np.array(
        [
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 1, 1, 0],
            [1, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    )

    k = np.array([0.5, 0.5, 20, 0.0001, 15, 1, 2])
    x0 = np.array([1, 0, 0, 0])
    t_max = 30

    output = ssa.output.ArrayOutput(np.linspace(0, t_max, 1000))

    x_names = ["inactive promoter", "active promoter", "mRNA", "protein"]

    model = ssa.Model(
        reactants=reactants, products=products, k=k, x0=x0, t_max=t_max, output=output
    )
    result = model.simulate(n_reps=1)
    ssa.plot(result, x_names=x_names, show=False)
    plt.savefig("two_state_gene_expression.png")


run()
