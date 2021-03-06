import numpy as np
import math
import matplotlib.pyplot as plt

V   = np.linspace(0, 30, num=10000) # X axis

I_0 = math.pow(10,-12) # saturation current
I_l = 2.7 # current generated by the photoelectric effect

q_by_kb = 11594 # electron charge / Boltzmann constant

abs_temp = 500 # absolute temperature

# Shockley solar cell equation
I_pv = I_l - (I_0 * (np.exp(q_by_kb*V / (abs_temp)) -1))

# plotting the result using matplotlib
plt.plot(V, I_pv)
plt.tight_layout()
plt.show()
