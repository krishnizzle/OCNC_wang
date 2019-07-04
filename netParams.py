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

netParams.importCellParams(label='INH',conds={'cellType':'INH'}, fileName='cells/INH_cell.py',
                           cellName='MakeCell',cellInstance=True)

##Population parameters
netParams.popParams['I']={'cellType': 'INH', 'numCells': 100, 'cellModel' : 'HH'}



print(netParams.popParams)


## Synaptic mechanism parameters
#This time in the mod file there is a POINT PROCESS because this is a point thing, not distributed over the whole neuron
#netParams.synMechParams['inh'] = {'mod': 'fvpre'}  
# inhibitory synaptic mechanism

# Stimulation parameters
#netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 10, 'noise': 0.5}
netParams.stimSourceParams['Iin'] = {'type': 'IClamp', 'delay': 20, 'dur': 500, 'amp': 0.02}
netParams.stimTargetParams['Iin->INH'] = {'source': 'Iin', 'conds': {'cellType': 'INH'}, 'sec': 'soma', 'loc':0.5}
