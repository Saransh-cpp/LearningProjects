import pybamm

model = pybamm.lithium_ion.DFN()

print(model.options)

model = pybamm.lithium_ion.DFN(
    options=None
)

solver = pybamm.ScikitsDaeSolver()

sim = pybamm.Simulation(model, solver=solver)
sim.solve([0, 3700])
sim.plot()

print(model.options)