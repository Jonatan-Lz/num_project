import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
import math
import sys

b_am = input("Type in amount of celestial bodies: ")
# steps = int(input("Type in amount of steps: "))
steps = 200
formatted_b_am = b_am.zfill(5)
filename = f'ellipse_N_{formatted_b_am}'
fetchdata = f'./Nbody/Nbody/input_data/{filename}.gal'

data=np.fromfile(fetchdata ,dtype=float)


debug = False

def bug_print(text):
    if debug:
        print(text)

N = int(round(data.size / 6))
G = 100/N
E = 0.001
dt = 0.00001

X = 0
Y = 1

pos = np.zeros((N, 2))

m = np.zeros(N)

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
# to clarify, i typed all this out, this wasn't AI made


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
        F_temp[i] = F
 
    for i in range(N):
        A = F_temp[i]/m[i]
        vel[i][X] += dt * A[0]
        vel[i][Y] += dt * A[1]
        
        pos[i][X] += dt * vel[i][X]
        pos[i][Y] += dt * vel[i][Y]

def save_result_to_file(steps, filename):
    # pos, b, vel, ps 
    result = np.zeros(6 * N, dtype=float)
    counter = 0
    for i in range(N):
        result[counter] = pos[i][X]
        result[counter + 1] = pos[i][Y]
        result[counter + 2] = m[i]
        result[counter + 3] = vel[i][X]
        result[counter + 4] = vel[i][Y]
        result[counter + 5] = b[i]
        counter += 6
    result_filename = filename + '_output.gal'
    result.tofile(result_filename)

def main():
    for i in range(steps):
        sim_step()
    save_result_to_file(steps, filename)
    
main()