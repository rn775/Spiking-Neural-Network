#!/usr/local/bin/python3
from brian2 import *
import numpy as np
import matplotlib.pyplot as plt
import placeCells
#import medium
from time import gmtime, strftime

prefs.codegen.target = "numpy"

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
I : amp (constant)
selected_index : integer (shared)  # single variable
'''

'''
If neuron 0 has an input voltage AND cell0 = True, excite neuron 1
If neuron 0 has an input voltage AND cell1 = True, excite neuron 2
If neuron 0 has an input voltage AND cell2 = True, excite neuron 3
If neuron 0 has an input voltage AND cell3 = True, excite neuron 4
'''

# 1st to 2nd layer
G = NeuronGroup(5, lif, threshold='v > -40*mV',
                reset='v = vl', refractory=5*ms, method='euler')
G.I = [0.7, 0, 0, 0, 0]*nA      # input current for 0, 1, 2, 3, 4 neurons
G.v = [-70, -70, -70, -70, -70]*mV    # intial voltage for 0, 1, 2, 3, 4 neurons (resting V)

# Se = excitory connection
# Si = inhibitory connection
#print(placeCells.cell0, placeCells.cell1, placeCells.cell2, placeCells.cell3)
# every 20ms, select a random index between 1 and 4
#G.run_regularly('selected_index = 1 + int(rand()*4)', dt=20*ms, when='end')

#G.run_regularly('maze()', dt=20*ms, when='start')

def maze():
    placeCells.createtheBackground()
    placeCells.run_Maze()
    print(placeCells.cell0, placeCells.cell1, placeCells.cell2, placeCells.cell3)
    print("Running?:", placeCells.isRunning)

maze()

if placeCells.placeCell0==True:
    G.run_regularly('selected_index = 1', dt=20*ms, when='end')
    print("\n             neuron 1", placeCells.placeCell0, placeCells.isRunning, strftime("%H:%M:%S", gmtime()))

if placeCells.placeCell1==True:
    G.run_regularly('selected_index = 2', dt=20*ms, when='end')

if placeCells.placeCell2==True:
    G.run_regularly('selected_index = 3', dt=20*ms, when='end')

if placeCells.placeCell3==True:
    G.run_regularly('selected_index = 4', dt=20*ms, when='end')

# Propagate spikes to all neurons, but multiply the weight with 0 or 1
# depending whether the postsynaptic index ('j') equals the selected index
Se = Synapses(G, G, on_pre='ge_post += w_ge * int(selected_index_post == j)')


Se.connect(i=0, j=[1, 2, 3, 4])

'''
if bool(placeCells.cell1)==False:
    G.run_regularly('selected_index = 2')
Si = Synapses(G, G, on_pre='gi_post += w_gi * int(selected_index_post == j)')
Si.connect(i=1, j=2)
'''

M = StateMonitor(G, 'v', record=True)

def runNN():
    run(1000*ms)

    fig, ax = plt.subplots(1)
    ax.plot(M.t/ms, M.v[0]/mV, color='white')
    ax.plot(M.t/ms, M.v[1]/mV, color='orange')
    ax.plot(M.t/ms, M.v[2]/mV, color='green')
    ax.plot(M.t/ms, M.v[3]/mV, color='red')
    ax.plot(M.t/ms, M.v[4]/mV, color='purple')

    ax.set_xlabel('time (ms)')
    ax.set_ylabel('voltage (mV)')
    ax.legend(('N0', 'N1', 'N2', 'N3', 'N4'))
    plt.show()

runNN()
placeCells.other()
