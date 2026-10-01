import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
import math
import sys

# Input prompt for the user
b_am = input("Type in amount of celestial bodies: ")
formatted_b_am = b_am.zfill(5)

# The input file is determined by the input of the user of this program
filename = f'ellipse_N_{formatted_b_am}'
fetchdata = f'./Nbody/Nbody/input_data/{filename}.gal'

# Fetch data from from input file
data=np.fromfile(fetchdata ,dtype=float)

# Amount of timesteps the simulation takes
steps = 200

# Define how many planets N based in input
N = int(round(data.size / 6))

# Gravity constant
G = 100/N

# Constant given in assignment
E = 0.001

# Timestep
dt = 0.00001

# Constants making array indexes easier to read
X = 0
Y = 1

# 2D array for bodies positions
pos = np.zeros((N, 2))

# 1D array for mass
m = np.zeros(N)

# 2D array for bodies velocities
vel = np.zeros((N, 2))

# 1D array for brightness
b = np.zeros(N)

# 2D array containing the force on all bodies in a timestep
F_temp = np.zeros((N, 2))

# For loop adding data to arrays above
i = 0
for val in data:
    if i % 6 == 0:
        pos[i // 6][0] = val
    elif i % 6 == 1:
        pos[i // 6][1] = val
    elif i % 6 == 2:
        m[i // 6] = val
    elif i % 6 == 3:
        vel[i // 6][0] = val
    elif i % 6 == 4:
        vel[i // 6][1] = val
    elif i % 6 == 5:
        b[i // 6] = val
    i += 1

# Printing initial data
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


# Function simulating a single timestep in a simulation
def sim_step():
    # For each planet    
    for i in range(N):
        # Vector for force
        f_sum = np.zeros(2)
        
        for j in range(N):

            #This if statements skips calculating the force a body exerts upon itself
            if(i == j):
                continue
            
            # Calculate the force upon a body using distance and mass
            R_ij = np.array([pos[i][0] - pos[j][0], pos[i][1] - pos[j][1]])
            r_ij = np.sqrt((pos[i][0] - pos[j][0])**2 + (pos[i][1] - pos[j][1])**2)
            f_sum += (m[j]/(r_ij + E)**3)*R_ij
        
        # Add the force exterted on a body to the array holding a forces in a timespte
        F = -G*m[i]*f_sum
        F_temp[i] = F
 
    # This for loop calculates and updates the acceleration, velocities and positions of all planets
    for i in range(N):
        A = F_temp[i]/m[i]
        vel[i][X] += dt * A[0]
        vel[i][Y] += dt * A[1]
        
        pos[i][X] += dt * vel[i][X]
        pos[i][Y] += dt * vel[i][Y]


# Function saving and storing our result into a gal file in accordance to format specified in assignment
def save_result_to_file(steps, filename):
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
    
    # Output file named after the input data
    result_filename = filename + '_output.gal'
    result.tofile(result_filename)

# Main function
def main():
    # Running the simulation for each timestep
    for i in range(steps):
        sim_step()

        # Print to check what timestep the simulation is on during runtime
        # We found this helpful for the more computationally heavy simulations
        print(i)

    # Store result into a result file in the same directory
    save_result_to_file(steps, filename)
    
main()