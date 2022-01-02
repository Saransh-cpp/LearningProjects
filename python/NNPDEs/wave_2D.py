import matplotlib.pyplot as plt
import numpy as np

import deepxde as dde
from deepxde.backend import tf


nu_ref = 0.1

x_min = 0
x_max = 1
y_min = 0
y_max = 1
t_min = 0
t_max = 1
n = 1
L = 1


def pde(x, u):
    u_tt = dde.grad.hessian(u, x, i=2, j=2)
    u_xx = dde.grad.hessian(u, x, i=0, j=0)
    u_yy = dde.grad.hessian(u, x, i=1, j=1)
    return u_tt - nu_ref * (u_xx + u_yy)


# def func(x):
#     return (
#         np.sin(np.pi * x[:, 0:1])
#         * np.sin(np.pi * x[:, 1:2])
#         * np.exp(-2 * nu_ref * np.pi ** 2 * x[:, 2:3])
#     )


def boundary_u(x, on_boundary):
    return on_boundary and np.isclose(x[1], 1)


def boundary_b(x, on_boundary):
    return on_boundary and np.isclose(x[1], 0)


def boundary_r_and_l(x, on_boundary):
    return on_boundary and (np.isclose(x[0], 0) or np.isclose(x[0], 1))


geom = dde.geometry.Rectangle(xmin=[x_min, y_min], xmax=[x_max, y_max])
timedomain = dde.geometry.TimeDomain(t_min, t_max)
geomtime = dde.geometry.GeometryXTime(geom, timedomain)

d_bc_b = dde.DirichletBC(geomtime, lambda x: np.sin(n * np.pi * x[:, 0:1] / L), boundary_b)
d_bc_u = dde.DirichletBC(geomtime, lambda x: 0, boundary_u)
n_bc = dde.NeumannBC(geomtime, lambda X: 0, boundary_r_and_l)

data = dde.data.TimePDE(
    geomtime,
    pde,
    [
        d_bc_u,
        d_bc_b,
        n_bc
    ],
    num_domain=2540,
    num_boundary=80,
    num_initial=160,
    num_test=2540,
)

layer_size = [3] + [20] * 3 + [1]
activation = "tanh"
initializer = "Glorot uniform"
net = dde.maps.FNN(layer_size, activation, initializer)
# net.apply_output_transform(
#     lambda x, u: u
#     * x[:, 2:3]
#     * x[:, 0:1]
#     * (1 - x[:, 0:1])
#     * x[:, 1:2]
#     * (1 - x[:, 1:2])
#     + tf.sin(np.pi * x[:, 0:1]) * tf.sin(np.pi * x[:, 1:2])
# )

model = dde.Model(data, net)

model.compile("adam", lr=0.001)
model.train(epochs=20000)
model.compile("L-BFGS")
losshistory, train_state = model.train()

dde.saveplot(losshistory, train_state, issave=True, isplot=True)
