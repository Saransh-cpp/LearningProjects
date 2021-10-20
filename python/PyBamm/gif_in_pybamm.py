import pybamm

sim = pybamm.Simulation(model=pybamm.lithium_ion.SPM())
sim.solve([0, 3600])
plot = pybamm.QuickPlot(sim)
plot.dynamic_plot()
plot.create_gif()