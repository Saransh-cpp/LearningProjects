import pybamm
import numpy as np
import matplotlib.pyplot as plt

pybamm.set_logging_level("NOTICE")
experiment = pybamm.Experiment(
    ['Discharge at 1 C until 3.5 V', 'Charge at 2 C until 3.9 V', 'Hold at 3.9 V until 91 mA'] * 26,
    termination="80% capacity"
)
model = pybamm.lithium_ion.SPMe(
    {
        "SEI": "reaction limited"
    }
)

sim = pybamm.Simulation(model, experiment=experiment, parameter_values=pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Marquis2019), solver=pybamm.CasadiSolver(mode="fast with events"))
sim.solve()
solution = sim.solution
vars_to_plot = [
        "Capacity [A.h]",
        "Loss of lithium inventory [%]",
        "Loss of capacity to negative electrode SEI [A.h]",
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

fig, axes = plt.subplots(n, m, figsize=(10, 10))
for var, ax in zip(vars_to_plot, axes.flat):
    ax.plot(
        solution.summary_variables["Cycle number"],
        solution.summary_variables[var]
    )
    ax.set_xlabel("Cycle number")
    ax.set_ylabel(var)
    ax.set_xlim([1, solution.summary_variables["Cycle number"][-1]])
fig.tight_layout()
plt.show()

