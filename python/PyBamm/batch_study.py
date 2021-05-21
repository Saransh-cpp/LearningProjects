import pybamm

model = pybamm.BatchStudy(
    permutations=True,
    models={"DFN": pybamm.lithium_ion.DFN(),
        "SPM": pybamm.lithium_ion.SPM()
    },
    parameter_values={"Chen2020": pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020),
    "Chen2020": pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)}
    # solvers={"casadi safe": pybamm.CasadiSolver(mode="safe")}
    )

model.solve(t_eval=[0, 3600])
model.plot()

dfn = pybamm.lithium_ion.DFN()

parameter_values = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)

sim = pybamm.Simulation(model=dfn, parameter_values=parameter_values)

sim.solve(t_eval=[0, 3600])

sim.plot()