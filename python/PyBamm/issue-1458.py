import numpy as np
import pybamm

def my_current(t):
    return pybamm.sin(2 * np.pi * t / 60)

chemistry = pybamm.parameter_sets.Chen2020

parameter_values = pybamm.ParameterValues(chemistry=chemistry)

parameter_values["Current function [A]"] = my_current

model = pybamm.lithium_ion.SPMe()
sim = pybamm.Simulation(model, parameter_values=parameter_values)
t_eval = np.arange(0, 121, 1)
print(t_eval)
sim.solve([0, 3700])
sim.plot(["Current [A]", "Terminal voltage [V]"])