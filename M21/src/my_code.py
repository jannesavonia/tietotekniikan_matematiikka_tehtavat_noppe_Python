"""
M09

Kirjoita funktiot T(dx) ja S(c), jotka palauttavat matriisit, jotka
vastaavat siirrosta dx:n kanssa ja skaalausta vakiolla c
"""
import numpy as np 

def T(dx):
    #Your code here
    
def S(c):
    #Your code here


#Test software
if __name__=='__main__':
    import random as rnd 
    epsilon=0.0001

    for i in range(100):
        x=np.array([rnd.gauss(1, 5), 1])
        x_real=x[0]
        for _ in range(10):
            c=rnd.gauss(1, 5)
            dx=rnd.gauss(1, 2)
            x=T(dx)@x
            x=S(c)@x
            x_real=x_real+dx
            x_real=x_real*c

        assert np.abs(x[0]-x_real)<epsilon