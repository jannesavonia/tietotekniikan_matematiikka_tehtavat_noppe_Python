"""
M28

x(0)=[1]
     [0]

v(0)=[0]
     [1]
 
a(x)=(-1.25/||x||)*x-0.3*v

Kirjoita funktio ab_spiral(Dt, n), joka tallentaa tekstitiedostoon output.txt jokaisella aika-askelella:
    t_i = ajanhetki, ensimmäinen 0 ja viimeinen n*Dt
    x_i = ajanhetkeä vastaava x-koordinaatti
    y_i = ajanhetkeä vastaava y-koordinaatti.
Sarakkeet erotetaan välilyönnillä. Tiedostossa on siis n+1 riviä.

Parametrit:
    Dt = aika-askel
    n = aika-askeleiden lukumäärä

Ratkaisussa käytetään luentokalvoissa esitettyä 2. kertaluvun Adams-Bashforth-menetelmää.
Käynnistä laskenta Eulerin menetelmällä.
"""

import os
import numpy as np 

filename=os.path.dirname(__file__)+'/output.txt'

def save(outf, x, t):
    x_i=x[0]
    y_i=x[1]
    outf.write(f'{t} {x_i} {y_i}\n')


def ab_spiral(Dt, n):
    #Your code here

if __name__=='__main__':
    import pandas as pd
    from matplotlib import pyplot as plt 

    show_figure=False

    if show_figure:
        N=100
        dt=10/N
        ab_spiral(dt, N)
        data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])
        plt.plot(data['x'], data['y'], label=f'Dt={dt}')

        N=1000
        dt=10/N
        ab_spiral(dt, N)
        data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])
        plt.plot(data['x'], data['y'], label=f'Dt={dt}')

        N=10000
        dt=10/N
        ab_spiral(dt, N)
        data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])
        plt.plot(data['x'], data['y'], label=f'Dt={dt}')

        plt.legend()
        plt.show()

    N=100
    dt=10/N
    ab_spiral(dt, N)
    data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])

    inaccurate_values=np.array([[4.3, 0.3348311043562908, -0.10543010657264017],
                                 [6.7,  -0.025926510426994766, -0.2557111932731299]])
    
    accurate_values=np.array([[4.3,  0.33590747680361643, -0.08836541262642196],
                              [6.7,  -0.019781308150982085, -0.2621123367635826]])

    assert len(data)==N+1, 'length of data error'
    assert len(data.columns)==3, 'columns number error'

    eps=0.0001
    assert abs(data['t'].min()-0)<eps
    assert abs(data['t'].max()-N*dt)<eps

    def compare_xy(data, t, x, y):
        d=data.loc[(t-eps<data['t']) & (data['t']<t+eps)]
        dx=float(d['x'])
        dy=float(d['y'])
        return abs(dx-x), abs(dy-y)
    
    for t, x, y in inaccurate_values:
        dx,dy=compare_xy(data, t, x, y)
        assert dx<eps
        assert dy<eps

    N=10000
    dt=10/N
    ab_spiral(dt, N)
    data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])
    for t, x, y in accurate_values:
        dx,dy=compare_xy(data, t, x, y)
        assert dx<eps
        assert dy<eps

