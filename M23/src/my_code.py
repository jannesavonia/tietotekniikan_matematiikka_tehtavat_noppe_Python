"""
M11
Kirjoita funktio direction(a, b), joka saa parametrina kaksi homogeenisen 
koordinaatiston paikkavektoria. Funktio palauttaa yksikkösuuntavektorin a:sta b:hen.
"""
import numpy as np 

def direction(a, b):
    #Your code here
    

#Test software
if __name__=='__main__':
    import random as rnd 
    epsilon=0.0001

    for i in range(500):
        a=np.random.randn(3)
        a=np.append(a, [1])
        b=np.random.randn(3)
        b=np.append(b, [1])
        if np.linalg.norm(a-b)<epsilon:
            continue

        x=direction(a,b)
        z=a-b
        assert abs(z@x+np.linalg.norm(z))<epsilon
        
