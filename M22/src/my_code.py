"""
M10

Kirjoita funktio unitnormal(a, b), jossa a ja b ovat R^3:n vektoreita 
(ei homogeenisissa koordinaateissa). Funktio palauttaa a:n ja b:n virittämän tason 
yksikkönormaalin, eli yksikkövektorin, joka on molempia vektoreita vasten kohtisuorassa.
"""
import numpy as np 

def unitnormal(a, b):
    #Your code here
    

#Test software
if __name__=='__main__':
    import random as rnd 
    epsilon=0.0001

    for i in range(500):
        a=np.random.randn(3)
        b=np.random.randn(3)
        if np.linalg.norm(a)<epsilon or np.linalg.norm(b)<epsilon:
            continue

        normal=unitnormal(a, b)
        minus_normal=unitnormal(b, a)

        #Check a x b = -b x a
        assert np.linalg.norm(normal+minus_normal)<epsilon
        
        #Check perpindicularity
        assert np.abs(a@normal)<epsilon
        assert np.abs(b@normal)<epsilon

        #Check length
        assert np.abs(np.linalg.norm(normal)-1)<epsilon

        
