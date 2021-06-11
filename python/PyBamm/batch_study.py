import pybamm

param1 = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)

param1["Current function [A]"] = 5

experiment = {
        "0": pybamm.Experiment(
        [
            ("Discharge at C/10 for 10 hours or until 3.3 V",
            "Rest for 1 hour",
            "Charge at 1 A until 4.1 V",
            "Hold at 4.1 V until 50 mA",
            "Rest for 1 hour")
        ]
        * 3,
    )
}

model = pybamm.BatchStudy(
    permutations=True,
    models={
        "0": pybamm.lithium_ion.DFN(),
        "1": pybamm.lithium_ion.SPM(),
        "2": pybamm.lithium_ion.SPMe(),
    },
    parameter_values={
        "param1": param1,
    },
    experiments=experiment
)
print("yes")

model.solve()
print("yes")

for sim in model.sims:
    print(sim.solution["Time [s]"].entries)

import Math

print(Math.max())
print("yes")

plot = pybamm.QuickPlot(model.sims, time_unit="seconds")
plot.plot(10)
plot.fig.savefig("a.png", dpi=300)
