import matplotlib.pyplot as plt
import numpy as np

import deepxde as dde
from deepxde.backend import tf

b = 0.1
c = 0.1
a = 0.1
L = 1
n = 1
# alpha_1 = 1
# alpha_2 = 1
# c_n = 1


def pde(x, u):
    """
    Expresses the PDE residual of the telegraph equation.
    """
    u_t = dde.grad.jacobian(u, x, i=0, j=1)
    u_xx = dde.grad.hessian(u, x, i=0, j=0)
    u_tt = dde.grad.hessian(u, x, i=0, j=1)
    return u_tt + (a * u_t) + (b * u) - ((c ** 2) * u_xx)


# def sol(x):
#     x, t = np.split(x, 2, axis=1)
#     return c_n * (np.exp(alpha_1 * t) - (alpha_1 / alpha_2) * np.exp(alpha_2 * t)) * np.sin(np.pi * x * L)


# Computational geometry:
geom = dde.geometry.Interval(0, L)
timedomain = dde.geometry.TimeDomain(0, 1)
geomtime = dde.geometry.GeometryXTime(geom, timedomain)

# Initial and boundary conditions:
bc = dde.DirichletBC(geomtime, lambda x: 1, lambda _, on_boundary: on_boundary)
bc_r = dde.NeumannBC(geom, lambda X: 0, lambda _, on_boundary: on_boundary)
ic = dde.IC(
    geomtime,
    # lambda x: np.sin(n * np.pi * x[:, 0:1] / L),
    lambda x: 0,
    lambda _, on_initial: on_initial,
)

data = dde.data.TimePDE(
    geomtime,
    pde,
    [bc, bc_r, ic],
    num_domain=2540,
    num_boundary=80,
    num_initial=160,
    num_test=2540,
    # solution=sol
)
net = dde.nn.FNN([2] + [20] * 3 + [1], "tanh", "Glorot normal")
model = dde.Model(data, net)

# Build and train the model:
model.compile("adam", lr=1e-3)
model.train(epochs=20000)
model.compile("L-BFGS")
losshistory, train_state = model.train()

# Plot/print the results
dde.saveplot(losshistory, train_state, issave=True, isplot=True)
