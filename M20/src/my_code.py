"""
M08

Kirjoita funktio projection(x, y), joka palauttaa x:n
projektion y:lle. Jos y on 0-vaktori, niin heitetään poikkeus.
"""

import numpy as np 

def projection(x, y):
    #Your code here
    

#Test software
if __name__=='__main__':
    epsilon=0.0001

    def check(x, y):
        proj=projection(x, y)
        perpendicular=(np.abs((x-proj)@y)<epsilon)
        same_dir=np.abs(np.abs(y@proj)-(np.linalg.norm(y)*np.linalg.norm(proj)))<epsilon
        return perpendicular, same_dir

    for i in range(3, 30):
        print(32*'-')
        x=np.random.randn(i)
        y=np.random.randn(i)
        print(f'x={x}')
        print(f'y={y}')
        perp, dir=check(x, y)
        assert perp, 'x-Px was not perpendicular to y'
        assert dir, '||Px|| was not correct, or Px was not parallel to y'
