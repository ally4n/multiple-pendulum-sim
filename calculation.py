import numpy as np

def simulate_pendulum_chain(lengths, masses, initial_angles, time_step, total_time):
    # Constants
    g = 9.81  # m/s^2

    # Initial conditions
    thetas = initial_angles
    omegas = np.zeros_like(thetas)

    # Time array
    t = np.arange(0, total_time, time_step)

    # Simulation loop
    for i in range(len(t)):
        # Calculate acceleration
        alpha = np.zeros_like(thetas)
        for j in range(len(thetas)):
            if j == 0:
                alpha[j] = -g / lengths[j] * np.sin(thetas[j])
            else:
                alpha[j] = -g / lengths[j] * np.sin(thetas[j]) + g / lengths[j] * np.sin(thetas[j-1])

        # Update velocity and position
        omegas += alpha * time_step
        thetas += omegas * time_step

        # Calculate energy
        kinetic_energy = 0.5 * masses * lengths**2 * omegas**2
        potential_energy = masses * g * lengths * (1 - np.cos(thetas))
        energy = np.sum(kinetic_energy) + np.sum(potential_energy)

        # Return results
        yield thetas, omegas, energy
