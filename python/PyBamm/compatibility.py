import pybamm

model = pybamm.lithium_ion.SPMe()

params = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)
params1 = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Marquis2019)

sim = pybamm.BatchStudy({"SPMe": model}, parameter_values={"Chen2020": params, "Marquis2019": params1}, experiments={
    "0": pybamm.Experiment([
            (
                "Discharge at C/10 for 10 hours "
                + "or until 3.3 V",
                "Rest for 1 hour",
                "Charge at 1 A until 4.1 V",
                "Hold at 4.1 V until 50 mA",
                "Rest for 1 hour"
            )
        ])
},
permutations=True)

sim.solve([0, 3700])
sim.plot()

# DFN - X - Mohtat2020, Sulzer2019
# SPM - X - Mohtat2020, Prada2013, Sulzer2019
# SPMe - X - Mohtat2020, Prada2013, Sulzer2019