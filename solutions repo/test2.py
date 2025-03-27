import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
M = 5.97e24  # Mass of Earth in kg

# Orbital radii (in meters)
radii = np.linspace(1e7, 1e9, 100)

# Calculate orbital periods using Kepler's Third Law
T = 2 * np.pi * np.sqrt(radii**3 / (G * M))

# Plot the relationship between T^2 and r^3
plt.figure(figsize=(8, 6))
plt.plot(radii**3, T**2, label="T^2 vs r^3", color='b')
plt.xlabel("r^3 (m^3)")
plt.ylabel("T^2 (s^2)")
plt.title("Kepler's Third Law: Orbital Period vs Orbital Radius")
plt.grid(True)
plt.legend()
plt.show()
