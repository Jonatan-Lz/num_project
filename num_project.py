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

debug = False

def bug_print(text):
    if debug:
        print(text)

# bug_print(data)

N = int(round(data.size / 6))
G = 100/N
E = 0.001
dt = 0.00005

X = 0
Y = 1

# bug_print(N)

# x_pos = np.zeros(N)
# y_pos = np.zeros(N)

pos = np.zeros((N, 2))

m = np.zeros(N)

# x_vel = np.zeros(N)
# y_vel = np.zeros(N)

vel = np.zeros((N, 2))

b = np.zeros(N)

F_temp = np.zeros((N, 2))

i = 0
for val in data:
    if i % 6 == 0:
        pos[i // 6][0] = val
    elif i % 6 == 1:
        pos[i // 6 - 1][1] = val
    elif i % 6 == 2:
        m[i // 6] = val
    elif i % 6 == 3:
        vel[i // 6][0] = val
    elif i % 6 == 4:
        vel[i // 6 - 1][1] = val
    elif i % 6 == 5:
        b[i // 6] = val
    i += 1

def print_data():
    print(f'xy_pos = {pos}')
    print(f'xy_vel = {vel}')
    print(f'mass = {m}')

print_data()


# Steps for simulation:
# for each planetary body:
# 1. Calculate normalized distance vector by using these formulas:
# e_x, y_x = ???
# a) R_ij = (x_i - x_j)*e_x + (y_i - y_j)*e_y
# b) r_ij = np.sqrt(x_i - x_j)**2 + (y_i - y_j)**2
# c) r_norm = R_ij/r_ij
#
# 2. Calculate force exerted upon celestial body by other bodies:
# F = -G*m_i * SUM(m_j/((r_ij + E)**3)*R_ij)
# here, SUM(m_j/((r_ij + E)**3)*R_ij) is the force all other bodies exert upon this one
# 
# 3. Update celestial body data:
# a) a_i = F/m_i
# b) vel_i += dt*a_i
# c) pos_i += dt*vel_i

def sim_step():
    for i in range(N):
        f_sum = np.zeros(2)
        for j in range(N):
            if(i == j):
                continue
            
            R_ij = np.array([pos[i][0] - pos[j][0], pos[i][1] - pos[j][1]])
            # bug_print(f"R_ij = {R_ij}")
            
            r_ij = np.sqrt((pos[i][0] - pos[j][0])**2 + (pos[i][1] - pos[j][1])**2)
            
            # r_norm = R_ij/r_ij
            
            f_sum += (m[j]/(r_ij + E)**3)*R_ij
            
        F = -G*m[i]*f_sum
        # print(F)
        
        F_temp[i] = F
        
        # print(F_temp[i])
 
    for i in range(N):
        A = F_temp[i]/m[i]
        vel[i][X] += dt * A[0]
        vel[i][Y] += dt * A[1]
        
        pos[i][X] += dt * vel[i][X]
        pos[i][Y] += dt * vel[i][Y]

steps = 10000
# planet1 = np.zeros((steps, 2))
# planet2 = np.zeros((steps, 2))

planetx = np.zeros(steps)
planety = np.zeros(steps)

planeta = np.zeros(steps)
planetb = np.zeros(steps)

for i in range(steps):
    sim_step()
    print(f'x1 = {pos[0][X]}, x2 = {pos[1][X]}')
    print(f'y1 = {pos[0][Y]}, y2 = {pos[1][Y]}')
    print("---")
    
    planetx[i] = pos[0][X]
    planety[i] = pos[0][Y]

    planeta[i] = pos[1][X]s
    planetb[i] = pos[1][Y]
    
    # planet1[i][X] = pos[0][X]
    # planet1[i][Y] = pos[0][Y]
    # planet2[i][X] = pos[1][X]
    # planet2[i][Y] = pos[1][Y]
    
    # print(pos[0][X], pos[0][Y])
    # print(pos[1][X], pos[1][Y])

# print_data()

plt.plot(planetx, planety, "-b")
plt.plot(planeta, planetb, "-r")
# plt.plot(planet2[X], planet2[Y], "-r")
plt.savefig("Test1")