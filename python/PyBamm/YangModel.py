import pybamm
import matplotlib.pyplot as plt

pybamm.set_logging_level("NOTICE")
model = pybamm.lithium_ion.Yang2017()
parameter_values = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Yang2017)
experiment = pybamm.Experiment(
    [(
      "Discharge at 2C until 2.8V",
      "Rest for 5 minutes",
      "Charge at 1C until 4.2V",
      "Hold at 4.2V until C/10",
      "Rest for 5 minutes",)] * 5,
)
sim =  pybamm.Simulation(model, experiment = experiment, parameter_values=parameter_values)
solution = sim.solve( solver=pybamm.CasadiSolver(mode="safe"))
sim.plot()

experiment = pybamm.Experiment(
     [(
       "Discharge at 0.02C until 2.8V (10 minute period)",
       "Rest for 5 minutes",
      "Charge at 0.1C until 4.2V (20 minute period)",
       "Hold at 4.2V until C/10 (10 minute period)",
       "Rest for 5 minutes",)] * 5,
 )
sim =  pybamm.Simulation(model, experiment = experiment, parameter_values=parameter_values)
solution = sim.solve( solver=pybamm.CasadiSolver(mode="safe"))

t_sol = solution["Time [s]"].entries
d_sol = 1000*solution["Discharge capacity [A.h]"].entries
fig = plt.figure("Time")
plt.plot(t_sol, solution["Terminal voltage [V]"](t_sol), '--')
fig = plt.figure("Capacity")
plt.plot(d_sol, solution["Terminal voltage [V]"](t_sol),'--', color = 'red')
plt.show()

