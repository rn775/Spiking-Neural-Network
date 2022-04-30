#!/usr/local/bin/python3
from brian2 import *
import numpy as np
import matplotlib.pyplot as plt

start_scope()

# Neuronal Parameters
c = 100*pF
vl = -70*mV
gl = 5*nS

# Synaptic Parameters
ge_tau = 20*ms
ve = 0*mV
gi_tau = 100*ms
vi = -80*mV
w_ge = 1.0*nS
w_gi = 0.1*nS # N1 inhibitory weight, N1 inhibits N2 to an extent that prevents the spike

# euler method
# dge & dgi describe change of the excitatory and inhibitory synaptic conductances
lif = '''
dv/dt = -(gl * (v - vl) + ge * (v - ve) + gi *(ve - vi) - I)/c : volt
dge/dt = -ge / ge_tau : siemens
dgi/dt = -gi / gi_tau : siemens
I : amp
'''

# 1st to 2nd layer
G = NeuronGroup(5, lif, threshold='v > -40*mV',
                reset='v = vl', refractory=3*ms, method='euler')
G.I = [0.7, 0.5, 0, 0, 0]*nA      # input current for 0, 1, 2 neurons, (0 & 1 are input neurons)
G.v = [-70, -70, -70, -70, -70]*mV    # intial voltage for 0, 1, 2 neurons (resting V)

# Se = excitory connection
# Si = inhibitory connection
Se = Synapses(G, G, on_pre='ge_post += w_ge')
Se.connect(i=0, j=2)
Se.connect(i=1, j=2)
Se.connect(i=2, j=3)
Se.connect(i=3, j=4)

Si = Synapses(G, G, on_pre='gi_post += w_gi')
Si.connect(i=1, j=2)

M = StateMonitor(G, 'v', record=True)

run(100*ms)

fig, ax = plt.subplots(1)
ax.plot(M.t/ms, M.v[0]/mV)
ax.plot(M.t/ms, M.v[1]/mV)
ax.plot(M.t/ms, M.v[2]/mV)
ax.plot(M.t/ms, M.v[3]/mV)
ax.plot(M.t/ms, M.v[4]/mV)

ax.set_xlabel('time (ms)')
ax.set_ylabel('voltage (mV)')
ax.legend(('N0', 'N1', 'N2', 'N3', 'N4'))
plt.show()
