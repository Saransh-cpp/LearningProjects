import pybamm

model = pybamm.lithium_ion.SPMe()

params = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)

sim = pybamm.BatchStudy({"SPMe": model}, parameter_values={"Chen2020": params})

sim.solve([0, 3700])
sim.plot()

# DFN - X - Mohtat2020, Sulzer2019
# SPM - X - Mohtat2020, Prada2013, Sulzer2019
# SPMe - X - Mohtat2020, Prada2013, Sulzer2019