import pybamm
import pandas as pd
import numpy as np
from pprint import pprint
from pybamm.q

model = pybamm.lithium_ion.DFN()
params = model.parameters

pprint(params)

# drive_cycle = pd.read_csv("US06.csv", comment="#", header=None).to_numpy()

# experiment = pybamm.Experiment(operating_conditions=["Run US06"], drive_cycles={"US06": drive_cycle}, period="20 seconds")

# sim = pybamm.Simulation(model, experiment=experiment, solver=pybamm.CasadiSolver(mode="fast"))

# sim.solve()
# solution = sim.solution

# pybamm.dynamic_plot(solution)
# solver = pybamm.CasadiSolver()
experiment = pybamm.Experiment(
    [
        ("Discharge at C/10 for 10 hours or until 3.3 V",
        "Rest for 1 hour",
        "Charge at 1 A until 4.1 V",
        "Hold at 4.1 V until 50 mA",
        "Rest for 1 hour")
    ]
    * 3,
)

sim = pybamm.Simulation(model)
print("yes")
sim.solve([0, 3700])
print("yes")
sim.plot()
# solution = sim.solution

# pybamm.dynamic_plot(solution)
