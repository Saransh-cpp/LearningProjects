import pybamm

output_variables = [
    "Capacity [A.h]",
    "Loss of lithium inventory [%]",
    "Loss of active material in negative electrode [%]",
    "Loss of active material in positive electrode [%]",
    "x_100",
    "x_0",
    "y_100",
    "y_0",
]

sim = pybamm.Simulation(model=pybamm.lithium_ion.DFN())

sim.solve([0, 3700])
sim.plot(output_variables=output_variables)