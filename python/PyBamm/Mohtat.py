import pybamm


pybamm.set_logging_level("NOTICE")
model = pybamm.lithium_ion.SPM()
params = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Mohtat2)
print(params["Lower voltage cut-off [V]"])
print(params["Upper voltage cut-off [V]"])
experiment = pybamm.Experiment(
    [
        (
            "Discharge at 1 A until 3.1 V",
            "Rest for 1 hour",
            "Charge at 0.01 A until 3.8 V",
            # "Hold at 4.1 V until 50 mA",
            # "Rest for 1 hour",
        )
    ]
    * 3,
)
sim = pybamm.Simulation(model, parameter_values=params, experiment=experiment)
sim.solve()
sim.plot()
