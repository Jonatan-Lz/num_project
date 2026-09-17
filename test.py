#williams lekhörna

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import math

G = 6.67430e-11
E = 1e-10

N = 3

m = np.array([1.0, 1.0, 1.0])

def force(x, v, t):
    F = -G* m_i *np.sum(m_j/(r_ij + E)**3 * R_ij)
    return F

def ode(t, y):
    a = np.zeros((N, 2))
    p = y[:,N]
    v = y[N,:]
    F = force(y[0], v, t)

    return [v, a]
    