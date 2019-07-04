#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:16:43 2019

@author: krishnizzle
"""
import numpy as np


import sys 
sys.path.append('/Applications/NEURON-7.6/nrn/lib/python')

from neuron import h

class INH_cell:
    
    soma=h.Section(name='soma')
    soma.L = 10/np.pi
    soma.diam = 10
    soma.Ra = 100
    soma.cm = 1
    
    soma.insert('naf')
    soma.insert('kdr')
    soma.insert('pas')
    
    
def MakeCell():
    cell = INH_cell()
    return cell


    
    

    
    
    
    
    
    
    
    
    
    
#cellRule['secs']['soma']['mechs']['pas'] = {'g': 0.0001, 'e': -65 }      # passive leak 

