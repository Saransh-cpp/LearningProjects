import numpy as np
import pybamm
from pprint import pprint

full_model = pybamm.BaseModel(name="full model")

R = pybamm.Parameter("Particle radius [m]")
D = pybamm.Parameter("Diffusion coefficient [m2.s-1]")
j = pybamm.Parameter("Interfacial current density [A.m-2]")
F = pybamm.Parameter("Faraday constant [C.mol-1]")
c0 = pybamm.Parameter("Initial concentration [mol.m-3]")

c = pybamm.Variable("Concentration [mol.m-3]", domain="negative particle")
c_av = pybamm.Variable("Average concentration [mol.m-3]")

N = -D * pybamm.grad(c)  # flux
dcdt = -pybamm.div(N)
full_model.rhs = {c: dcdt} 

full_model.initial_conditions = {c: c0}

lbc = pybamm.Scalar(0)
rbc = -j / F / D
full_model.boundary_conditions = {c: {"left": (lbc, "Neumann"), "right": (rbc, "Neumann")}}

full_model.variables = {
    "Concentration [mol.m-3]": c,
    "Surface concentration [mol.m-3]": pybamm.surf(c),
    "Average concentration [mol.m-3]": pybamm.r_average(c),
}

param = pybamm.ParameterValues(
    {
        "Particle radius [m]": 10e-6,
        "Diffusion coefficient [m2.s-1]": 3.9e-14,
        "Interfacial current density [A.m-2]": 1.4,
        "Faraday constant [C.mol-1]": 96485,
        "Initial concentration [mol.m-3]": 2.5e4,
    }
)

# r = pybamm.SpatialVariable("r", domain=["negative particle"], coord_sys="spherical polar")
# geometry = {"negative particle": {r: {"min": pybamm.Scalar(0), "max": R}}}
# param.process_geometry(geometry)

param.process_model("full model")

# def my_current(t):
#     return pybamm.sin(2 * np.pi * t / 60)

# chemistry = pybamm.parameter_sets.Chen2020

# parameter_values = pybamm.ParameterValues(chemistry=chemistry)

# parameter_values["Current function [A]"] = my_current

# model = pybamm.lithium_ion.SPMe()
# sim = pybamm.Simulation(model, parameter_values=parameter_values)
# t_eval = np.arange(0, 121, 1)
# print(t_eval)
# sim.solve([0, 3700])
# sim.plot(["Current [A]", "Terminal voltage [V]"])