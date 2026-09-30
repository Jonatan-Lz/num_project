import numpy as np
import matplotlib.pyplot as plt

filename = "./Nbody/Nbody/result_output/ellipse_N_00100_output.gal"

# Read binary .gal file
data = np.fromfile(filename, dtype=np.float64)

# Each particle has 6 doubles
N = len(data) // 6

# Reshape into one row per particle:
# [x, y, mass, vx, vy, brightness]
particles = data.reshape(N, 6)

x = particles[:, 0]
y = particles[:, 1]

# Plot particle positions
plt.figure(figsize=(8, 8))
plt.scatter(x, y, s=5)

plt.xlabel("x")
plt.ylabel("y")
plt.title(f"N-body simulation after 200 steps (N={N})")

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.gca().set_aspect("equal")

plt.grid(True)

plt.savefig("galaxy_after_200_steps.png", dpi=300, bbox_inches="tight")
plt.close()

print("Saved galaxy_after_200_steps.png")