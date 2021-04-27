import pybamm

params = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)
x = pybamm.linspace(3000,6000,100)
params.plot(values=["Negative electrode exchange-current density [A.m-2]", "Electrolyte conductivity [S.m-1]"])



