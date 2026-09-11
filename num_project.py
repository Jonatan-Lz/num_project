import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
import math

ans = input()

import numpy as np
data=np.fromfile("ans",dtype=float)
print(data)
# data.tofile("sol_N_2.gal")



N = 0
G = 100/N
E = 0.001
dt = 0.00005

x_pos = np.zeros(N)
y_pos = np.zeros(N)

x_vel = np.zeros(N)
y_vel = np.zeros(N)

m = np.zeros(N)


# 
def ode(y, t):
    np.zeros(2)
    yder = np.zeros(1)
    


