#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 19:59:22 2019

@author: krishnizzle
"""


import sys 
sys.path.append('/Applications/NEURON-7.6/nrn/lib/python')

from netpyne import specs, sim

import numpy as np

# Network parameters
netParams = specs.NetParams() #object of class netParams to store the network parameters

##Population parameters
netParams.popParams['I']={'celltype': 'INH', 'numCells': 100, 'cellModel' : 'HH'}
#netParams.popParams['M']={'celltype': 'PYR', 'numCells': 20, 'cellModel' : 'HH'}

print(netParams.popParams)

cellRule = {'conds': {'cellype': 'INH'}, 'secs': {}} 
cellRule['secs']['soma'] = {'geom': {}, 'mechs': {}}
cellRule['secs']['soma']['geom'] = {'diam': 10, 'L': 10/np.pi, 'Ra': 100}    
#in the .mod file, there is a SUFFIX, the name goes after mechs                                                           # soma geometry
cellRule['secs']['soma']['mechs']['naf'] = {}      # Na+ channel
cellRule['secs']['soma']['mechs']['kdr'] = {}      # K+ channel
cellRule['secs']['soma']['mechs']['pas'] = {}      # passive leak 


## Synaptic mechanism parameters
#This time in the mod file there is a POINT PROCESS because this is a point thing, not distributed over the whole neuron
netParams.synMechParams['inh'] = {'mod': 'fvpre'}  
# inhibitory synaptic mechanism

# Stimulation parameters
#netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5}

#netParams.stimTargetParams['bkg->PYR'] = {'source': 'bkg', 'conds': {'cellType': 'PYR'}, 'weight': 0.01, 'delay': 5, 'synMech': 'exc'}

## Cell connectivity rules

#netParams.connParams['S->M'] = { #  S -> M label
#        'preConds': {'pop': 'S'}, # conditions of presyn cells
#        'postConds': {'pop': 'M'}, # conditions of postsyn cells
#        'probability': 0.5,             # probability of connection
'''        'weight': 0.01,                         # synaptic weight
        'delay': 5,                                     # transmission delay (ms)
        'synMech': 'exc'}               # synaptic mechanism
'''