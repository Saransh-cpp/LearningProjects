from lorenz import solve_lorenz
from ipywidgets import interactive, fixed

w = interactive(solve_lorenz,sigma=(0.0,50.0),rho=(0.0,50.0))

t, x_t = w

xyz_avg = x_t.mean(axis=1)
print(xyz_avg)

num1 = 
num = 