import time
import sim
import numpy as np

# Example usage
lengths = [1, 1, 2, 0.5, 1.5] #lengths of pendulums
masses = [2, 1, 5, 12, 32] #masses of pendulums
initial_angles = [0.1, 0.2, 0.7, 0.9, 1.5] #initial radians of pendulums
time_step = 1 #time interval between each simulation step
total_time = 100 # determines the total amount of time that the simulation will run for. It is used to calculate the position of the pendulum at each time step

sim.render_pendulum_chain(lengths=np.array(lengths), masses=np.array(masses), initial_angles=np.array(initial_angles), time_step=time_step, total_time=total_time)
