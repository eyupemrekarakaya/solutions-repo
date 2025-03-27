import numpy as np
import matplotlib.pyplot as plt

# Constants
A = 1               # Amplitude
lambda_ = 1         # Wavelength
k = 2 * np.pi / lambda_  # Wave number
omega = 2 * np.pi   # Angular frequency (for simplicity, let's assume f = 1 Hz)
phi = 0             # Initial phase
num_sources = 4     # Number of sources (vertices of the square)
size = 10           # Size of the grid for visualization

# Coordinates of the square vertices
# Placing the sources at the vertices of a square
sources = np.array([
    [0, 0],
    [0, size],
    [size, 0],
    [size, size]
])

# Function to calculate the displacement at a point (x, y) due to a source at (x_s, y_s)
def wave_displacement(x, y, x_s, y_s):
    r = np.sqrt((x - x_s)**2 + (y - y_s)**2)  # Distance from source
    return A * np.cos(k * r - omega * 0 + phi)  # Time = 0 for simplicity

# Generate a grid of points to calculate the interference pattern
x_vals = np.linspace(-1, size + 1, 400)
y_vals = np.linspace(-1, size + 1, 400)
X, Y = np.meshgrid(x_vals, y_vals)

# Calculate total displacement at each point on the grid
Z = np.zeros_like(X)
for (x_s, y_s) in sources:
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] += wave_displacement(X[i, j], Y[i, j], x_s, y_s)

# Plotting the interference pattern
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, levels=50, cmap="RdBu_r")
plt.colorbar(label="Displacement (Amplitude)")
plt.title("Interference Pattern from 4 Sources (Square Configuration)")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
