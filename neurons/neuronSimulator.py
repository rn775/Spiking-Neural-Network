#!/usr/local/bin/python3
from spine import LIF, PoissonSpike
from spine.tools.plotting import plot_spike_scatter

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    duration = 500  # [ms]Experiment time
    dt = 0.1        # [ms] time step

    time = int(duration / dt)

    # Input data from Poisson Spike Gen.
    #Generate a Poisson spike sequence to be input from a random number
    spikes = PoissonSpike(np.random.random(10),
                          time=duration,
                          dt=dt).spikes

    #Appropriate weight
    weights = np.random.random(10) + 5.0

    #Define LIF neurons(Double exp filter)
    neu = LIF(duration,
              dt,
              k='double',  # use double exponential filter
              )

    #Calculate the membrane potential by passing the input spike sequence and weight
    #Returns membrane potential, output spike, ignition time
    v, s, f = neu.calc_v((spikes, weights))

    # Plot
    t = np.arange(0, duration, dt)

    plt.subplot(2, 1, 1)
    plot_spike_scatter(spikes, duration, dt, title='input spike trains', xlabel=None)

    plt.subplot(2, 1, 2)
    plt.plot(t, v)
    plt.plot(t, np.full_like(t, neu.th), linestyle='dashed')
    plt.ylabel('Membrane Voltage [mV]')
    plt.xlabel('time [ms]')
    plt.xlim(0, duration)

    plt.show()
