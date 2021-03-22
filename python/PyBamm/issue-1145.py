import pybamm

param = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Marquis2019)
model_1D_lumped = pybamm.lithium_ion.SPMe({"dimensionality": 1,
                                           "current collector": "potential pair",
                                           "thermal": "x-lumped"})
sim_1D_lumped = pybamm.Simulation(model_1D_lumped, parameter_values=param)
sim_1D_lumped.solve([0, 36])
temp = sim_1D_lumped.solution["Cell temperature [K]"].entries
t_min = temp.min()
t_max = temp.max()
variable_limits = {"X-averaged cell temperature [K]": "tight",
                   "Cell temperature [K]": "fixed",
                   "Volume-averaged cell temperature [K]": "tight"}
print(t_min, t_max)
sim_1D_lumped.plot(["X-averaged cell temperature [K]",
                    "Cell temperature [K]",
                    "Volume-averaged cell temperature [K]"],
                    variable_limits="tight",
                    )