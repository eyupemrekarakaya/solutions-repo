import numpy as np

# Constants
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
M_sun = 1.989e30  # Mass of Sun in kg
r_sun = 1.496e11  # Distance from Earth to Sun in meters

# Parameters for Earth, Mars, and Jupiter
celestial_bodies = {
    "Earth": {
        "mass": 5.97e24,  # in kg
        "radius": 6.37e6  # in meters
    },
    "Mars": {
        "mass": 6.42e23,
        "radius": 3.39e6
    },
    "Jupiter": {
        "mass": 1.90e27,
        "radius": 6.99e7
    }
}

def calculate_velocities(body_name, mass, radius):
    # First Cosmic Velocity (Orbital)
    v_orbital = np.sqrt(G * mass / radius)
    
    # Second Cosmic Velocity (Escape)
    v_escape = np.sqrt(2 * G * mass / radius)
    
    # Third Cosmic Velocity (Escape from the Sun)
    v_solar_escape = np.sqrt(2 * G * M_sun / r_sun)
    
    return v_orbital, v_escape, v_solar_escape

# Calculate for each body
results = {}
for body_name, params in celestial_bodies.items():
    v_orbital, v_escape, v_solar_escape = calculate_velocities(body_name, params['mass'], params['radius'])
    results[body_name] = {
        "Orbital Velocity (m/s)": v_orbital,
        "Escape Velocity (m/s)": v_escape,
        "Solar Escape Velocity (m/s)": v_solar_escape
    }

# Display results
for body_name, velocities in results.items():
    print(f"Velocities for {body_name}:")
    for key, value in velocities.items():
        print(f"{key}: {value:.2f} m/s")
    print()
