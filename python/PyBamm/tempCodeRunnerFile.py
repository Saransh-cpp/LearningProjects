model.print_parameter_info()

model.variables = {
    "v+f": v + pybamm.FunctionParameter("f", {"Time [s]": pybamm.t})
}
from pprint import pprint
pprint(model.parameters)

model.print_parameter_info()