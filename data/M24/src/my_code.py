"""
M12

Kirjoita funktio rotate_around_point(alpha, point, X), joka kiertää alpha:n verran homogeenisia
koordinaatteja X pisteen point ympäri vastapäivään. point on paikkavektori ja X ssisältää 1...N
paikkavektoria.

Funktio palauttaa muunnetut pisteet matriisissa. Kaikki pisteet ovat R^2 pisteitä, jotka on
upotettu homogeeniseen koordinaatistoon.
"""

import numpy as np 

def rotate_around_point(alpha, point, X):
    #Your code here

#Test software
if __name__=='__main__':
    import random as rnd 
    epsilon=0.0001

    for i in range(100):
        point=np.random.randn(2)
        point=np.append(point, [1])
        N=i
        X=np.random.randn(3, N)
        X[-1, :]=1 #Set 3rd coordinate as 1
        
        a=rnd.gauss(0, 16*np.pi)
        Z=rotate_around_point(a, point, X)

        for i in range(N):
            x=X[:, i]
            z=Z[:, i]
            #Check center of rotation
            assert abs(np.linalg.norm(point-x)-np.linalg.norm(point-z))<epsilon

            #Check rotation angle
            b=np.arccos(((x-point)@(z-point))/(np.linalg.norm(z-point)**2))
            assert abs(np.cos(b)-np.cos(a))<epsilon
