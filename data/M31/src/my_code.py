"""
M31

Toteuta solver(T). Katso tarkempi tehtävä luentokalvoista. 

"""

import os
import numpy as np 

filename=os.path.dirname(__file__)+'/output.txt'

def save(outf, x, t):
    x_i=x[0]
    y_i=x[1]
    outf.write(f'{t} {x_i} {y_i}\n')

def solver(T):
    #Your code here

if __name__=='__main__':
    import pandas as pd
    from matplotlib import pyplot as plt 

    show_figure=True #Set False to hide figure

    solver(20)
    data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])

    if show_figure:
        plt.plot(data['x'], data['y'], '*')
        plt.show()

    print(data)

    eps=0.01    
    for idx, row in data.iterrows():
        assert abs(idx-row['t'])<0.001, f'Sould be saved on integer t. idx={idx}, t={row["t"]}'
        t=row['t']
        x_correct=2.0*np.cos(t)
        y_correct=2.0*np.sin(t)
        x_computed=row['x']
        y_computed=row['y']
        
        diff=np.array([x_computed-x_correct, y_computed-y_correct])
        diff_norm=np.linalg.norm(diff)
        print(t, x_correct, x_computed, y_correct, y_computed, diff, diff_norm)
        assert diff_norm<eps


