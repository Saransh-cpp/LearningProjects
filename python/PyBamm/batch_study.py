import pybamm

model = pybamm.BatchStudy(
    permutations=True,
    models={"Yang2017": pybamm.lithium_ion.DFN(),
        "NewmanTobias": pybamm.lithium_ion.SPMe()
    },
    )

model.solve(t_eval=[0, 3600])
model.plot()

model = pybamm.lithium_ion.Yang2017()

sim = pybamm.Simulation(model)
sim.solve([0, 3700])
sim.plot()