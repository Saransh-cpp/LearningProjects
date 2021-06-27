import pybamm

param1 = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)
param1['Negative electrode exchange-current density [A.m-2]'] = 4

param2 = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Chen2020)
param2["Negative electrode exchange-current density [A.m-2]"] = 5

parameter_values = {
    "param1": param1,
    "param2": param2
}

s = pybamm.BatchStudy(
    {
        "DFN": pybamm.lithium_ion.DFN(),
    },
    experiments={
        "cccv": pybamm.Experiment(
            [
                (
                    "Discharge at C/10 for 10 hours or until 3.3 V",
                    "Rest for 1 hour",
                    "Charge at 1 A until 4.1 V",
                    "Hold at 4.1 V until 50 mA",
                    "Rest for 1 hour",
                )
            ]
        )
    },
    parameter_values=parameter_values,
    permutations=True
)

s.solve()
labels = ["1", "2"]
plot = pybamm.QuickPlot(s.sims, labels=labels)
plot.plot(10)
plot.fig.savefig("plot877.png", dpi=300)