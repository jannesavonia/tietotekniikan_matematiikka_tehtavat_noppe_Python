"""
M01

v(t)=[-sin t]
     [cos t]

x(0)=[1]
     [0]

Kirjoita funktio euler_circle(Dt, n), joka kirjoittaa tekstitiedostoon output.txt jokaisella aika-askelella:
    t_i = ajanhetki, ensimmäinen 0 ja viimeinen n*Dt
    x_i = ajanhetkeä vastaava x-koordinaatti
    y_i = ajanhetkeä vastaava y-koordinaatti.
Sarakkeet erotetaan välilyönnillä. Tiedostossa on siis n+1 riviä.

Parametrit:
    Dt = aika-askel
    n = aika-askeleiden lukumäärä

Ratkaisussa käytetään luentokalvoissa esitettyä Euler-menetelmää.
"""

import os
import numpy as np 

filename=os.path.dirname(__file__)+'/output.txt'

def f(t, x):
    #Your code here

def euler_circle(Dt, n):
    #Your code here

    #Example of row to save values
    #outf.write(f'{t_i} {x_i} {y_i}\n')

if __name__=='__main__':
    import pandas as pd

    T=19
    dt=0.001
    N=int(T/dt)

    euler_circle(dt, N)
    data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])

    accurate_values=np.array([[3.3, np.cos(3.3), np.sin(3.3)],
                              [6.3, np.cos(6.3), np.sin(6.3)],
                              [18.9, np.cos(18.9), np.sin(18.9)]])

    assert len(data)==N+1, 'length of data error'
    assert len(data.columns)==3, 'columns number error'

    eps=0.001
    assert abs(data['t'].min()-0)<eps
    assert abs(data['t'].max()-N*dt)<eps

    def compare_xy(data, t, x, y):
        d=data.loc[(t-dt/2<data['t']) & (data['t']<t+dt/2)]
        data_x=float(d['x'])
        data_y=float(d['y'])
       
        return abs(data_x-x), abs(data_y-y)
    

    for t, x, y in accurate_values:
        dx,dy=compare_xy(data, t, x, y)
        assert dx<eps, "Accuracy error"
        assert dy<eps, "Accuracy error"
