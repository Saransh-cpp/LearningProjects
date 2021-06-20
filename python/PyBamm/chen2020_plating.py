import pybamm

sim = pybamm.Simulation(pybamm.lithium_ion.DFN(), parameter_values=pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020_plating))
sim.solve([0, 3700])
sim.plot()