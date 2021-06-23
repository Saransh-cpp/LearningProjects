import pybamm
import numpy as np
import matplotlib.pyplot as plt

pybamm.set_logging_level("NOTICE")
model = pybamm.lithium_ion.DFN(
    options={
        'lithium plating': 'reversible',
        'SEI porosity change': 'false'
    }
)

chemistry = pybamm.parameter_sets.Chen2020_plating

params = pybamm.ParameterValues(chemistry=chemistry)

experiment = pybamm.Experiment(
    [('Discharge at 3 C until 3.4 V', 'Charge at 1 C until 4.0 V', 'Hold at 4.0 V until 65 mA')] * 69
)

sim = pybamm.Simulation(
    model=model,
    experiment=experiment,
    parameter_values=params,
)

params["Lithium plating kinetic rate constant [m.s-1]"] = -10
sim.solve()
solution = sim.solution
solutions = [solution]

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
            solution.summary_variables[var]
        )
    ax.set_xlabel("Cycle number")
    ax.set_ylabel(var)
    ax.set_xlim([1, solution.summary_variables["Cycle number"][-1]])
fig.tight_layout()
plt.savefig("plot2.png", dpi=300)