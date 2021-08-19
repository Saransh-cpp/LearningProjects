import pybamm
import numpy as np
import matplotlib.pyplot as plt


def generate_summary_variables(chemistry, solutions, labels):
    """
    Creates and saves a picture of summary variable comparison plot.
    """
    if chemistry == pybamm.parameter_sets.Ai2020:  # pragma: no cover
        vars_to_plot = [
            "Measured capacity [A.h]",
            "Loss of lithium inventory [%]",
            "Loss of active material in negative electrode [%]",
            "Loss of active material in positive electrode [%]",
        ]
    else:
        vars_to_plot = [
            "Capacity [A.h]",
            "Loss of lithium inventory [%]",
            "Loss of active material in negative electrode [%]",
            "Loss of active material in positive electrode [%]",
            "x_100",
            "x_0",
            "y_100",
            "y_0",
        ]

    length = len(vars_to_plot)
    n = int(length // np.sqrt(length))
    m = int(np.ceil(length / n))

    fig, axes = plt.subplots(n, m, figsize=(15, 8))
    for var, ax in zip(vars_to_plot, axes.flat):
        for solution in solutions:
            ax.plot(
                solution.summary_variables["Cycle number"],
                solution.summary_variables[var],
            )
        ax.set_xlabel("Cycle number")
        ax.set_ylabel(var)
        ax.set_xlim([1, solution.summary_variables["Cycle number"][-1]])

    fig.tight_layout()
    fig.legend(labels, loc="lower left", bbox_to_anchor=(0.77, -0.08))
    plt.savefig("bug.png", dpi=300, bbox_inches="tight")


pybamm.set_logging_level("NOTICE")

models = {0: pybamm.lithium_ion.SPM({"SEI": "reaction limited"})}

chemistry = pybamm.parameter_sets.Chen2020

params1 = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)
params2 = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)
params3 = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)

params1["Ambient temperature [K]"] = 288.19
params2["Ambient temperature [K]"] = 351.13
params3["Ambient temperature [K]"] = 276.66

params = {0: params1, 1: params2, 2: params3}

experiment = pybamm.Experiment(
    [
        (
            "Discharge at 3 C until 3.3 V",
            "Charge at 3 C until 3.8 V",
            "Hold at 3.8 V until 63 mA",
        )
    ]
    * 14
)

experiments = {0: experiment}

labels = [
    "Ambient temperature [K]: 288.19",
    "Ambient temperature [K]: 351.13",
    "Ambient temperature [K]: 276.66",
]

s = pybamm.BatchStudy(
    models, parameter_values=params, experiments=experiments, permutations=True
)
s.solve()

solutions = [x.solution for x in s.sims]
generate_summary_variables(chemistry, solutions, labels,)
