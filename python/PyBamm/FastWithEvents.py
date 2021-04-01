import pybamm

model = pybamm.lithium_ion.DFN()
parameter_values = model.default_parameter_values

experiment = pybamm.Experiment(
    [
        "Discharge at 5 C until 3.9 V",
        "Charge at 2 C until 4.0 V",
        "Hold at 4.0 V until 83 mA",
        "Rest for 9 minutes",
        "Discharge at 5 C until 3.9 V",
        "Charge at 2 C until 4.0 V",
        "Hold at 4.0 V until 83 mA",
        "Rest for 9 minutes",
    ]
)
solver = pybamm.CasadiSolver(mode="safe")

sim = pybamm.Simulation(model, experiment=experiment, solver=solver)
sim.solve()
solution = sim.solution

pybamm.dynamic_plot(solution)