import pybamm

parameter_values = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Mohtat2020)
parameter_values.update({"SEI kinetic rate constant [m.s-1]": 1e-14})

spm = pybamm.lithium_ion.SPM({"SEI": "ec reaction limited"})
spme = pybamm.lithium_ion.SPMe({"SEI": "ec reaction limited"})
Vmin = 3.0
Vmax = 4.2
experiment = pybamm.Experiment(
    [
        (
            f"Discharge at 1C until {Vmin}V",
            "Rest for 1 hour",
            f"Charge at 1C until {Vmax}V",
            f"Hold at {Vmax}V until C/50",
        )
    ]
    * 3,
    termination="80% capacity",
)
sim = pybamm.Simulation(spm, experiment=experiment, parameter_values=parameter_values)
sol = sim.solve(initial_soc=1)
sim = pybamm.Simulation(spme, experiment=experiment, parameter_values=parameter_values)
sol1 = sim.solve(initial_soc=1)
pybamm.plot_summary_variables([sol, sol1], labels=["SPM", "SPMe"])
