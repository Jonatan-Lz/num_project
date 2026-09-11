#williams lekhörna

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import math

def ode(t, y):
    yder = np.zeros(1)

def sympeuler(f, tspan, u0, h):
    interval = round((tspan[1]-tspan[0])/h)
    tvec = np.linspace(tspan[0], tspan[1], interval + 1)
    u = np.zeros(len(tvec), len(u0))
    i = 0
    u0=u[i, :]
    for i in range(len(tvec)-1):

    