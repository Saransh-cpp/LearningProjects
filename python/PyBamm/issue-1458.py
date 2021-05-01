import numpy as np
import pybamm
from pprint import pprint

# full_model = pybamm.BaseModel(name="full model")

# R = pybamm.Parameter("Particle radius [m]")
# D = pybamm.Parameter("Diffusion coefficient [m2.s-1]")
# j = pybamm.Parameter("Interfacial current density [A.m-2]")
# F = pybamm.Parameter("Faraday constant [C.mol-1]")
# c0 = pybamm.Parameter("Initial concentration [mol.m-3]")

# c = pybamm.Variable("Concentration [mol.m-3]", domain="negative particle")
# c_av = pybamm.Variable("Average concentration [mol.m-3]")

# N = -D * pybamm.grad(c)  # flux
# dcdt = -pybamm.div(N)
# full_model.rhs = {c: dcdt}

# full_model.initial_conditions = {c: c0}

# lbc = pybamm.Scalar(0)
# rbc = -j / F / D
# full_model.boundary_conditions = {c: {"left": (lbc, "Neumann"), "right": (rbc, "Neumann")}}

# full_model.variables = {
#     "Concentration [mol.m-3]": c,
#     "Surface concentration [mol.m-3]": pybamm.surf(c),
#     "Average concentration [mol.m-3]": pybamm.r_average(c),
# }

# param = pybamm.ParameterValues(
#     {
#         "Particle radius [m]": 10e-6,
#         "Diffusion coefficient [m2.s-1]": 3.9e-14,
#         "Interfacial current density [A.m-2]": 1.4,
#         "Faraday constant [C.mol-1]": 96485,
#         "Initial concentration [mol.m-3]": 2.5e4,
#     }
# )

# r = pybamm.SpatialVariable("r", domain=["negative particle"], coord_sys="spherical polar")
# geometry = {"negative particle": {r: {"min": pybamm.Scalar(0), "max": R}}}
# param.process_geometry(geometry)

# param.process_model("full model")

# def my_current(t):
#     return pybamm.sin(2 * np.pi * t / 60)

# chemistry = pybamm.parameter_sets.Chen2020

# parameter_values = pybamm.ParameterValues(chemistry=chemistry)

# parameter_values["Current function [A]"] = my_current

# model = pybamm.lithium_ion.SPMe()
# model.parameters
# sim = pybamm.Simulation(model, parameter_values=parameter_values)
# t_eval = np.arange(0, 121, 1)
# print(t_eval)
# sim.solve([0, 3700])
# sim.plot(["Current [A]", "Terminal voltage [V]"])

# values = {
#     "Particle radius [m]": 10e-6,
#     "Diffusion coefficient [m2.s-1]": 3.9e-14,
#     "Interfacial current density [A.m-2]": 1.4,
#     "Faraday constant [C.mol-1]": 96485,
#     "Initial concentration [mol.m-3]": 2.5e4,
# }

# param = pybamm.ParameterValues(values)
# print(param)

# param.update(
#     {
#         "Particle radius [m]": 10e-7,
#     }
# )

# print(param)

# model = pybamm.lithium_ion.DFN()
# chemistry = pybamm.parameter_sets.Marquis2019
# parameter_values = pybamm.ParameterValues(chemistry=chemistry)

# sim = pybamm.Simulation(model=model, parameter_values=parameter_values)

# sim.solve([0, 3600])
# sim.plot()

# mydict = {
#     1: {
#         "negative tab": (2),
#         "positive tab": (3),
#     }
# }

# keys = mydict.values()
# print(keys)
# for key in keys:
#     if isinstance(key, dict):
#         if "positive tab" in key.keys():
#             side_list = ["positive tab", "negative tab", "no tab"]

# print(side_list)

# param = pybamm.ParameterValues(["a", 6])
# param.update
# import os

# print(os.path.exists("graphite_LGM50_ocp_Chen2020.csv"))
# load model
# model = pybamm.lithium_ion.BasicDFN()
# default_parameters = model.default_parameter_values

# # Read my anode parameters from csv file
# anode_param = pybamm.ParameterValues("parameters.csv")

# # Update parameter values
# orig_values = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)
# # print(orig_values)
# orig_values.update(anode_param) 

# print(orig_values == pybamm.parameter_sets.Chen2020)
import unittest
from unittest.mock import patch, call

# class TestFunc(unittest.TestCase):
#     @patch('builtins.print')
#     def test(self, mocked_print):
#         for cc_dimension in [0]:
#             geometry = pybamm.battery_geometry(current_collector_dimension=cc_dimension)
#         print(geometry.print_parameter_info())

#         # print(end='\r')
#         mocked_print.assert_called_with('Negative electrode thickness [m] (Parameter)')

# if __name__ == '__main__':
#     unittest.main()

# for cc_dimension in [0]:
#     geometry = pybamm.battery_geometry(current_collector_dimension=cc_dimension)
#     print(geometry.print_parameter_info(test=True))

# model = pybamm.BaseModel()
# a = pybamm.Parameter("a")
# b = pybamm.InputParameter("b", "test")
# c = pybamm.Parameter("c")
# d = pybamm.Parameter("d")
# e = pybamm.Parameter("e")
# f = pybamm.InputParameter("f")
# g = pybamm.Parameter("g")
# h = pybamm.Parameter("h")

# u = pybamm.Variable("u")
# v = pybamm.Variable("v")
# model.rhs = {u: -u * a}
# model.algebraic = {v: v - b}
# model.initial_conditions = {u: c, v: d}
# model.events = [pybamm.Event("u=e", u - e)]
# model.variables = {"v+f": v + f}
# model.boundary_conditions = {
#     u: {"left": (g, "Dirichlet"), "right": (0, "Neumann")},
#     v: {"left": (0, "Dirichlet"), "right": (h, "Neumann")},
# }

# model.variables = {
#     "v+f": v + pybamm.FunctionParameter("f", {"Time [s]": pybamm.t})
# }
# model.print_parameter_info()

var = pybamm.Variable("var")
model = pybamm.BaseModel()
model.algebraic = {var: var + pybamm.InputParameter("value")}
model.initial_conditions = {var: 2}

        # create discretisation
disc = pybamm.Discretisation()
disc.process_model(model)

        # Solve
solver = pybamm.AlgebraicSolver()
solution = solver.solve(model, np.linspace(0, 1, 10), inputs={"value": 7})
model.print_parameter_info()
