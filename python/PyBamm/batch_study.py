import pybamm

param1 = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Yang2017)
param2 = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Yang2017)
param3 = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Yang2017)

param1["Current function [A]"] = 5
param2["Current function [A]"] = 1.5
param3["Current function [A]"] = 0.5

model = pybamm.BatchStudy(
    permutations=True,
    models={
        "0": pybamm.lithium_ion.DFN(),
    },
    parameter_values={
        "param1": param1,
        "param2": param2,
        "param3": param3
    }
)

model.solve(t_eval=[0, 3700])
model.plot()