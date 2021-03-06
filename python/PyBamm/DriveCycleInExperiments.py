import pybamm
import pandas as pd
import numpy as np

model = pybamm.lithium_ion.DFN()
params = model.default_parameter_values

drive_cycle = pd.read_csv("US06.csv", comment="#", header=None).to_numpy()

experiment = pybamm.Experiment(operating_conditions=["Run US06 (A) for 1 hour"], drive_cycles={"US06": drive_cycle}, period="20 seconds")

sim = pybamm.Simulation(model, experiment=experiment, solver=pybamm.CasadiSolver(mode="fast"))

sim.solve()
solution = sim.solution

pybamm.dynamic_plot(solution)