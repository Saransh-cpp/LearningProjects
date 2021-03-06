import pybamm

# params = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)
# i0 = params["Negative electrode exchange-current density [A.m-2]"]
# x = pybamm.linspace(3000,6000,100)
# params.evaluate(i0(1000,x,300))

model = pybamm.lithium_ion.DFN()
default_parameters = model.default_parameter_values

# Extracting parameter values
values = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)

# Exporting values to  csv file
values.export_csv(filename="export_param.csv")

# # Reading values from this csv file
# new_values = pybamm.ParameterValues("export_param.csv")
# load model
# model = pybamm.lithium_ion.BasicDFN()
# default_parameters = model.default_parameter_values

# # Read my anode parameters from csv file
# anode_param = pybamm.ParameterValues("./parameters.csv")

# # Update parameter values
# orig_values = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)
# orig_values.update(anode_param)

# print(orig_values)
