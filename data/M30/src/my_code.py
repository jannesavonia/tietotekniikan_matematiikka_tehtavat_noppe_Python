"""
M30

Ratkaise P'(t) = P(t)*(1-P(t)), kun P(0)=1/2
aikavälillä 0...10s. Tallenna arvot tasasekunteina tiedostoon.
"""

import os
import numpy as np 

filename=os.path.dirname(__file__)+'/output.txt'

def save(outf, P, t):
    outf.write(f'{int(t)} {P}\n')


#Your code here. Create a software, not a single function

#Test code 
import pandas as pd

data=pd.read_csv(filename, delimiter=' ', names=['t','P'])
P_estim=data['P'].to_numpy()

assert np.abs(P_estim[0]-0.5).max()<=0.00001, 'accuracy error'
assert np.abs(P_estim[3]-0.95257413).max()<=0.00001, 'accuracy error'
assert np.abs(P_estim[10]-0.9999546).max()<=0.00001, 'accuracy error'

