import pybamm

params = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)
i0 = params["Negative electrode exchange-current density [A.m-2]"]
x = pybamm.linspace(3000,6000,100)
i0_eval = i0(1000,x,300)
i0_processed = params.process_symbol(i0_eval)
pybamm.plot(x, i0_processed)

