import pybamm
import matplotlib.pyplot as plt
import numpy as np


def lico2_volume_change_Ai2020(sto):
    omega = pybamm.Parameter("Positive electrode partial molar volume [m3.mol-1]")
    c_p_max = pybamm.Parameter("Maximum concentration in positive electrode [mol.m-3]")
    t_change = omega * c_p_max * sto
    return t_change


def graphite_volume_change_Ai2020(sto):
    p1 = 145.907
    p2 = -681.229
    p3 = 1334.442
    p4 = -1415.710
    p5 = 873.906
    p6 = -312.528
    p7 = 60.641
    p8 = -5.706
    p9 = 0.386
    p10 = -4.966e-05
    t_change = (
        p1 * sto ** 9
        + p2 * sto ** 8
        + p3 * sto ** 7
        + p4 * sto ** 6
        + p5 * sto ** 5
        + p6 * sto ** 4
        + p7 * sto ** 3
        + p8 * sto ** 2
        + p9 * sto
        + p10
    )
    return t_change


pybamm.set_logging_level("NOTICE")
model = pybamm.lithium_ion.SPM(
    options={
        "particle mechanics": "swelling only",
    }
)
params = pybamm.ParameterValues(chemistry=pybamm.parameter_sets.Mohtat2020)
params.update(
    {
        # mechanical properties
        "Positive electrode Poisson's ratio": 0.3,
        "Positive electrode Young's modulus [Pa]": 375e9,
        "Positive electrode reference concentration for free of deformation [mol.m-3]": 0,
        "Positive electrode partial molar volume [m3.mol-1]": -7.28e-7,
        "Positive electrode volume change": lico2_volume_change_Ai2020,
        "Negative electrode volume change": graphite_volume_change_Ai2020,
        # Loss of active materials (LAM) model
        "Positive electrode LAM constant exponential term": 2,
        "Positive electrode critical stress [Pa]": 375e6,
        # mechanical properties
        "Negative electrode Poisson's ratio": 0.3,
        "Negative electrode Young's modulus [Pa]": 15e9,
        "Negative electrode reference concentration for free of deformation [mol.m-3]": 0,
        "Negative electrode partial molar volume [m3.mol-1]": 3.1e-6,
        # Loss of active materials (LAM) model
        "Negative electrode LAM constant exponential term": 2,
        "Negative electrode critical stress [Pa]": 60e6,
        # Other
        "Cell thermal expansion coefficient [m.K-1]": 1.48e-6,
        "SEI kinetic rate constant [m.s-1]": 1e-15,
        "Positive electrode LAM constant propotional term": 1e-3,
        "Negative electrode LAM constant propotional term": 1e-3,
        "EC diffusivity [m2.s-1]": 2e-18,
    },
    check_already_exists=False,
)
experiment = pybamm.Experiment(
    [
        (
            "Discharge at 3 C until 3.3 V",
            "Charge at 3 C until 3.8 V",
            "Hold at 3.8 V until 34 mA",
        )
    ]
    * 44
)

sim = pybamm.Simulation(
    model,
    parameter_values=params,
    experiment=experiment,
)
solution = sim.solve(initial_soc=1)

vars_to_plot = [
    "Capacity [A.h]",
    "Loss of lithium inventory [%]",
    "Loss of active material in negative electrode [%]",
    "Loss of active material in positive electrode [%]",
    "x_100",
    "x_0",
    "y_100",
    "y_0",
]

length = len(vars_to_plot)
n = int(length // np.sqrt(length))
m = int(np.ceil(length / n))

fig, axes = plt.subplots(n, m, figsize=(15, 8))
for var, ax in zip(vars_to_plot, axes.flat):
    ax.plot(
        solution.summary_variables["Cycle number"],
        solution.summary_variables[var],
    )
ax.set_xlabel("Cycle number")
ax.set_ylabel(var)
ax.set_xlim([1, solution.summary_variables["Cycle number"][-1]])

fig.tight_layout()
# fig.legend(self.labels, loc="lower left", bbox_to_anchor=(0.77, -0.08))
plt.plot()
plt.show()
# plt.savefig("plot.png", dpi=300, bbox_inches="tight")
