import pybamm
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

dfn = pybamm.lithium_ion.DFN()
spm = pybamm.lithium_ion.SPM()
params = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)

sim_dfn = pybamm.Simulation(dfn, parameter_values=params)
sim_dfn.solve([0, 3700])

sim_spm = pybamm.Simulation(spm, parameter_values=params)
sim_spm.solve([0, 3700])

pybamm.plot_voltage_components(sim_dfn.solution, ax=axes.flat[0])
pybamm.plot_voltage_components(sim_spm.solution, ax=axes.flat[0])

# fig.tight_layout()
axes.flat[0].set_title("DFN")
axes.flat[1].set_title("SPM")

plt.show()