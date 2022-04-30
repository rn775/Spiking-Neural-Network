#!/usr/local/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import random

T = 50    # total time to sumulate (msec)
dt = 0.0125  # Simulation timestep
time = int(T / dt)
inpt = 1.0   # Neuron input voltage
neuron_input = np.full((time), inpt)

num_layers = 2
num_neurons = 100


def plot_neuron_behaviour(time, data, neuron_type, neuron_id, y_title):
    # print ('Drawing graph with time.shape={}, data.shape={}'.format(time.shape, data.shape))
    plt.plot(time, data)
    plt.title('{} @ {}'.format(neuron_type, neuron_id))
    plt.ylabel(y_title)
    plt.xlabel('Time (msec)')
    # Graph to the data with some headroom...
    y_min = 0
    y_max = max(data)*1.2
    if y_max == 0:
        y_max = 1
    plt.ylim([y_min, y_max])
    plt.show()


def plot_membrane_potential(time, Vm, neuron_type, neuron_id=0):
    plot_neuron_behaviour(time, Vm, neuron_type, neuron_id, y_title='Membrane potential (V)')


def plot_spikes(time, Vm, neuron_type, neuron_id=0):
    plot_neuron_behaviour(time, Vm, neuron_type, neuron_id, y_title='Spike (V)')


class LIFNeuron():
    def __init__(self, debug=True):
        # Simulation config (may not all be needed!!)
        self.dt       = 0.125       # simulation time step
        self.t_rest   = 0           # initial refractory time

        #LIF Properties
        self.Vm       = np.array([0])    # Neuron potential (mV)
        self.time     = np.array([0])    # Time duration for the neuron
        self.spikes   = np.array([0])    # Output (spikes) for the neuron

        #self.output   = 0               # Neuron output
        self.t        = 0                # Neuron time step
        self.Rm       = 1                # Resistance (kOhm)
        self.Cm       = 10               # Capacitance (uF)
        self.tau_m    = self.Rm * self.Cm  # Time constant
        self.tau_ref  = 4                # refractory period (ms)
        self.Vth      = 0.75             # = 1  #spike threshold
        self.V_spike  = 1                # spike delta (V)
        self.type     = 'Leaky Integrate and Fire'
        self.debug    = debug
        if self.debug:
            print ('LIFNeuron(): Created {} neuron starting at time {}'.format(self.type, self.t))

    def spike_generator(self, neuron_input):
        # Create local arrays for this run
        duration = len(neuron_input)
        Vm = np.zeros(duration)  # len(time)) # potential (V) trace over time
        time = np.arange(self.t, self.t+duration)
        spikes = np.zeros(duration)  # len(time))

        if self.debug:
            print('spike_generator(): Running time period self.t={}, self.t+duration={}'
                   .format(self.t, self.t+duration))

        # Seed the new array with previous value of last run
        Vm[-1] = self.Vm[-1]

        if self.debug:
            print('LIFNeuron.spike_generator.initial_state(input={}, duration={}, initial Vm={}, t={})'
               .format(neuron_input, duration, Vm[-1], self.t))

        for i in range(duration):
            if self.debug:
                print('Index {}'.format(i))

            if self.t > self.t_rest:
                Vm[i]=Vm[i-1] + (-Vm[i-1] + neuron_input[i-1]*self.Rm) / self.tau_m * self.dt

                if self.debug:
                    print('spike_generator(): i={}, self.t={}, Vm[i]={}, neuron_input={}, self.Rm={}, self.tau_m * self.dt = {}'
                          .format(i,self.t, Vm[i], neuron_input[i], self.Rm, self.tau_m * self.dt))

                if Vm[i] >= self.Vth:
                    spikes[i] += self.V_spike
                    self.t_rest = self.t + self.tau_ref
                    if self.debug:
                        print('*** LIFNeuron.spike_generator.spike=(self.t_rest={}, self.t={}, self.tau_ref={})'
                           .format(self.t_rest, self.t, self.tau_ref))

            self.t += self.dt

        # Save state
        self.Vm = np.append(self.Vm, Vm)
        self.spikes = np.append(self.spikes, spikes)
        self.time = np.append(self.time, time)

        if self.debug:
            print ('LIFNeuron.spike_generator.exit_state(Vm={} at iteration i={}, time={})'
                   .format(self.Vm, i, self.t))

        #return time, Vm, output


def create_neurons(num_layers, num_neurons, debug=True):
    neurons = []
    for layer in range(num_layers):
        if debug:
            print('create_neurons(): Creating layer {}'.format(layer))
        neuron_layer = []
        for count in range(num_neurons):
            neuron_layer.append(LIFNeuron(debug=debug))
        neurons.append(neuron_layer)
    return neurons


neurons = create_neurons(num_layers, num_neurons, debug=False)


stimulus_len = len(neuron_input)
layer = 0
for neuron in range(num_neurons):
    offset = random.randint(0, 100)   # Simulates stimulus starting at different times
    stimulus = np.zeros_like(neuron_input)
    stimulus[offset:stimulus_len] = neuron_input[0:stimulus_len - offset]
    neurons[layer][neuron].spike_generator(stimulus)

plot_membrane_potential(neurons[0][0].time, neurons[0][0].Vm, 'Membrane Potential {}'.format(neurons[0][0].type), neuron_id="0/0")
plot_spikes(neurons[0][0].time, neurons[0][0].spikes, 'Output spikes for {}'.format(neurons[0][0].type), neuron_id="0/0")
