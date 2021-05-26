import pybamm

model = pybamm.BatchStudy(
    permutations=True,
    models={"0": pybamm.lithium_ion.DFN(),
        "1": pybamm.lithium_ion.SPMe()
    },
    )

model.solve(t_eval=[0, 3600])
model.plot()

model = pybamm.lithium_ion.Yang2017()

sim = pybamm.Simulation(model)
sim.solve([0, 3700])
sim.plot()