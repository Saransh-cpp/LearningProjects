import pybamm

model = pybamm.lithium_ion.DFN()
# create geometry
geometry = model.default_geometry

# load parameter values and process model and geometry
model.print_parameter_info()
param = model.parameters

param.process_geometry(geometry)
param.process_model(model)

print(param)

sim  = pybamm.Simulation(model)
sim.solve([0, 3700])
sim.plot()