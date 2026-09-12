import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
import math
import sys

# ans = input("Type in input data file: ")
# ans = "./Nbody/Nbody/input_data/" + ans

data=np.fromfile("./Nbody/Nbody/input_data/circles_N_2.gal" ,dtype=float)

# print(ans)
# print(data)
# data.tofile("sol_N_2.gal")
# data=np.fromfile("circles_N_2.gal",dtype=float)
# print(data)
# data.tofile("sol_N_2.gal")

print(data)

N = int(round(data.size / 6))
G = 100/N
E = 0.001
dt = 0.00005

print(N)

x_pos = np.zeros(N)
y_pos = np.zeros(N)

m = np.zeros(N)

x_vel = np.zeros(N)
y_vel = np.zeros(N)

b = np.zeros(N)

i = 0
def round_i(i):
    return math.ceil(i / 6) - 1

for val in data:
    if i % 6 == 0:
        x_pos[round_i(i)] = val
    if i % 6 == 1:
        y_pos[round_i(i)] = val
    if i % 6 == 2:
        m[round_i(i)] = val
    if i % 6 == 3:
        x_vel[round_i(i)] = val
    if i % 6 == 4:
        y_vel[round_i(i)] = val
    if i % 6 == 5:
        b[round_i(i)] = val
    i += 1

def print_data():
    print("x_positions: ", x_pos)
    print("y_positions: ", y_pos)
    print("x_velocity: ", x_vel)
    print("y_velocity: ", y_vel)
    print("mass: ", m)

print_data()


# 
def ode(y, t):
    np.zeros(2)
    yder = np.zeros(1)
