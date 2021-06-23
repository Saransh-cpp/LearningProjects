import pybamm

pybamm.set_logging_level("NOTICE")

model = {'0': pybamm.lithium_ion.DFN(
    options={
        "particle mechanics": "swelling and cracking",
    }
)
}
params = {'0': pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Ai2020)}

experiment = {'0': pybamm.Experiment(
    [
        ("Discharge at C/10 for 10 hours or until 3.3 V",
        "Rest for 1 hour",
        "Charge at 1 A until 4.1 V",
        "Hold at 4.1 V until 50 mA",
        "Rest for 1 hour")
    ]
    * 3,
)
}

sim = pybamm.BatchStudy(model, parameter_values=params, experiments=experiment)
sim.solve(calc_esoh=False)
sim.plot()