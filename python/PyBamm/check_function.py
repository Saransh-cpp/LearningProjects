import pybamm

param_to_vary_dict = {
    "Current function [A]": (None, None),
    "Electrode height [m]": (0.1, None),
    "Electrode width [m]": (0.1, None),
    "Negative electrode conductivity [S.m-1]": (None, None),
    "Negative electrode porosity": (None, None),
    "Negative electrode active material volume fraction": (None, None),
    "Negative electrode Bruggeman coefficient (electrolyte)": (None, None),
    "Negative electrode exchange-current density [A.m-2]": (None, None),
    "Positive electrode porosity": (None, None),
    "Positive electrode exchange-current density [A.m-2]": (None, None),
    "Positive electrode Bruggeman coefficient (electrolyte)": (None, None),
    "Ambient temperature [K]": (265, 355),
}

chemistries = [
    pybamm.parameter_sets.Chen2020,
    pybamm.parameter_sets.Marquis2019,
    pybamm.parameter_sets.Ai2020,
]

for x in chemistries:
    params = pybamm.ParameterValues(chemistry=x)
    print(x["citation"])
    for k in param_to_vary_dict:
        print(f"{k} - {params[k]}")
