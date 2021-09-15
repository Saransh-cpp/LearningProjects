import pybamm


model = pybamm.lithium_ion.DFN()
parameter_values = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)
# v = pybamm.Variable("v")
# p = pybamm.InputParameter("p")
# model.rhs = {v: -p}
# model.initial_conditions = {v: 1}
# model.variables = {
#     "v": v,
#     "2v": 2 * v,
#     "3v": 3 * v,
#     "4v": 4 * v,
#     "5v": 5 * v,
#     "6v": 6 * v,
#     "7v": 7 * v,
#     "8v": 8 * v,
# }

parameter_values["Current function [A]"] = 6
sim = pybamm.Simulation(model, parameter_values=parameter_values)
sim.solve([0, 3600])
# sim.plot()
# sim.solve([0, 3600], solver=pybamm.CasadiSolver(mode="safe"), inputs={"Crate": 1})
# sim.plot()
sim.interactive(
    [0, 3600],
    inputs={"Current [A]": 1.5},
    plot_kwargs={"output_variables": ["Current [A]", "Terminal voltage [V]"]},
)