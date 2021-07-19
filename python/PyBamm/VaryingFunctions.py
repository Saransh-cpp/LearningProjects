import pybamm
import random
import matplotlib.pyplot as plt

def desired_decimal_point_generator(start, stop, step):
    """
    Generates a random number with desired number
    of decimal digits.
    Parameters:
        start: numerical
        stop: numerical
        step: numerical
    Returns:
        rand_num: numerical
    """
    rand_num = round(random.uniform(start, stop), step)
    return rand_num

class FunctionLike:
    "Behaves like a function but saves fun and parameter"

    def __init__(self, fun, parameter):
        self.fun = fun
        self.parameter = parameter
        
    def __call__(self, *args):
        return self.parameter * self.fun(*args)        


def parameter_value_generator(chemistry, parameter):
    """
    Generates parameter values using the given chemistry and 
    updates the provided named parameter with a random value.
    Parameters:
        chemistry: dict
        parameter: str
    Returns:
        params: :class:`pybamm.ParameterValues`
    """
    params = pybamm.ParameterValues(chemistry=chemistry)

    if callable(params[parameter]):
        base_value = 1
        new_value = desired_decimal_point_generator(
            (base_value)*0.5, (base_value)*2, 2
        )            
        params[parameter] = FunctionLike(params[parameter], new_value)
    else:
        base_value = params[parameter]
        new_value = desired_decimal_point_generator(
            (base_value)*0.5, (base_value)*2, 2
        )    
        params[parameter] = new_value

    return params

chemistry=pybamm.parameter_sets.Marquis2019


parameter_values = {
    0: pybamm.ParameterValues(chemistry=chemistry),
    1: parameter_value_generator(chemistry, "Negative electrode exchange-current density [A.m-2]"),
}

# take a look at what the scaling is
print(parameter_values[0]["Negative electrode exchange-current density [A.m-2]"])
print(parameter_values[1]["Negative electrode exchange-current density [A.m-2]"].parameter)

# Negative electrode diffusivity [m2.s-1] is a function of sto and T, let's plot as a function of T
fig, ax = plt.subplots()
T = pybamm.linspace(200, 300, 20)
for p in parameter_values.values():
    D = p["Negative electrode exchange-current density [A.m-2]"]
    # sim = pybamm.Simulation(pybamm.lithium_ion.SPMe(), parameter_values=p)
    # sim.solve([0, 3700])
    # sim.plot(output_variables=["Negative electrode exchange current density [A.m-2]"])
    evaluated = p.evaluate(D(0.5, 1,T))
    plt.plot(T.entries, evaluated)

plt.show()

# sim = pybamm.BatchStudy({0: pybamm.lithium_ion.DFN()}, parameter_values=parameter_values, output_variables={0: "Negative electrode diffusivity [m2.s-1]"}, permutations=True)
# sim.solve([0, 3700])
# sim.plot()

# plt.show()
