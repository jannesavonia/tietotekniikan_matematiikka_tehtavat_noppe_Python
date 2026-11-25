"""
M06

Kirjoita funktio perpendicular, joka saa parametrinaan 
kaksi vektoria ja palauttaa True jos ne ovat kohtisuorassa
(jollain sopivalla tarkkuudella), muuten False.

Vektorin normin saat laskettua esimerkiksi np.linalg.norm-funktiolla
"""

import numpy as np 

def perpendicular(a, b):
    #Your code here returns True or False

if __name__=='__main__':
    #Test/example program, don't modify
    v1=np.array([0.01, 0.01, 0.01, 0.01], dtype=np.double)
    v2=np.array([1.e-6, 2.e-6, 1.e-6, -4.e-6], dtype=np.double)
    v3=np.array([-40, 20, 20, 0], dtype=np.double)
    v4=np.array([4, -2, -2, 0], dtype=np.double)
    v5=np.array([4.e6, -2.e6, 4.e6, 1.e6], dtype=np.double)

    assert perpendicular(v1, v2)
    assert perpendicular(v1, v3)
    assert perpendicular(v1, v4)
    assert perpendicular(v2, v5)
    assert perpendicular(v2, v1)
    assert perpendicular(v3, v1)
    assert perpendicular(v4, v1)
    assert perpendicular(v5, v2)
    assert perpendicular(v1, -v2)
    assert perpendicular(-v1, v3)
    assert perpendicular(v1, -v4)
    assert perpendicular(-v2, v5)
    assert perpendicular(v2, -v1)
    assert perpendicular(-v3, v1)
    assert perpendicular(v4, -v1)
    assert perpendicular(-v5, v2)
    assert not perpendicular(v2, v3)
    assert not perpendicular(v3, v4)
    assert not perpendicular(v1, v5)
    assert not perpendicular(v1, v1)
    assert not perpendicular(v2, v2)
    assert not perpendicular(v3, v3)
    assert not perpendicular(v4, v4)
    assert not perpendicular(v5, v5)
    assert not perpendicular(v1, -v1)
    assert not perpendicular(v2, -v2)
    assert not perpendicular(v3, -v3)
    assert not perpendicular(v4, -v4)
    assert not perpendicular(v5, -v5)

