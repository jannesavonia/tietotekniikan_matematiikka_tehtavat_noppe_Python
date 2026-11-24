"""
M9
Katso tehtävänanto luentokalvoista
"""

import os
import numpy as np

filename=os.path.dirname(__file__)+'/output.txt'

k=3
m=2
T=100

def save(outf, x, t):
    x_i=x[0]
    v_i=x[1]
    outf.write(f'{int(t)} {x_i}\n')

#Your code here
