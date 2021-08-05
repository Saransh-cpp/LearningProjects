import pybamm


model = pybamm.lithium_ion.DFN()
params = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)
# params.process_model(model)
model.variables["Negative electrode exchange current density [A.m-2]"].print_name
# a = pybamm.Symbol("a", domain="test")
# print(pybamm.Gradient(a).to_equation())
# print(params["Negative electrode exchange-current density [A.m-2]"].print_name())
# print(model.parameters)
# model.print_parameter_info()