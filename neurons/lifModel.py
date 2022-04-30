#!/usr/local/bin/python3
import numpy as np
import matplotlib.pyplot as plt


# setup parameters and state variables
T = 100                         # total time to simulate (msec)
dt = 0.1                        # simulation time step (msec)
time = np.arange(0, T+dt, dt)   # time array
t_rest = 0                      # initial refractory time

# LIF properties
V_m = np.zeros(len(time))       # potential (V) trace over time
R_m = 1                         # resistance (kOhm)
C_m = 10                        # capacitance (uF)
tau_m = R_m * C_m               # time constant (msec)
tau_ref = 4                     # refractory period (msec)
V_th = 1                        # spike threshold (V)
V_spike = 10.0                  # spike delta (V)

# stimulus
I_in = 2.0 * np.ones(len(time))  # input current (A)
noise = []                      # noise term

# iterate over each time step
for i, t in enumerate(time):
    if (t > t_rest):
        randomTerm = np.random.normal(0, 1)
        noise.append(randomTerm)
        V_m[i] = V_m[i-1] + (-V_m[i-1] + I_in[i]*R_m + randomTerm) / tau_m * dt
    if (t >= V_th):
        V_m[i] += V_spike
        t_rest = t + tau_ref

# plot membrane potential trace
plt.plot(time, V_m)
plt.title('Leaky Integrate-and-Fire Example')
plt.ylabel('Membrane Potential (V)')
plt.xlabel('Time (msec)')
plt.xlim(0, 100)
plt.ylim(-2, 12)
plt.show()
