import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
M = 5.97e24  # Mass of Earth in kg
R = 6371e3  # Radius of Earth in meters
m = 1.0  # Mass of payload in kg (can be neglected in force calculation)

# Initial conditions (example: 100 km altitude above Earth's surface)
initial_position = np.array([R + 100e3, 0])  # Position vector (in meters)
initial_velocity = np.array([0, 7.8e3])  # Velocity vector (in m/s, approx 7.8 km/s for circular orbit)

# Time settings
dt = 1  # Time step in seconds
t_max = 2 * 3600  # Total simulation time (2 hours)
steps = int(t_max / dt)

# Function to compute the gravitational acceleration
def gravitational_acceleration(position):
    r = np.linalg.norm(position)
    return -G * M * position / r**3

# Numerical integration using Euler method
positions = []
velocities = []
position = initial_position
velocity = initial_velocity

for _ in range(steps):
    acceleration = gravitational_acceleration(position)
    velocity += acceleration * dt
    position += velocity * dt
    positions.append(position)
    velocities.append(velocity)

positions = np.array(positions)

# Plot the trajectory
plt.figure(figsize=(8, 8))
plt.plot(positions[:, 0] / 1e3, positions[:, 1] / 1e3)  # Plot in km
plt.scatter(0, 0, color='red', label='Earth', s=100)  # Earth at the origin
plt.title("Trajectory of Freely Released Payload Near Earth")
plt.xlabel("X Position (km)")
plt.ylabel("Y Position (km)")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()
