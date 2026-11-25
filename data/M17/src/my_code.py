"""
M05

Lisää Vect-luokkaan pistetulo. Käytä pistetulon operaattorina @.
Jos vektoreiden dimensiot eivät ole samat, heitetään poikkeus.

Kopioi edellisen tehtävän Vect-luokka tähän pohjaksi.

"""

import math

class Vect:
    #Kopioi koodi tähän

    def __matmul__(self, v):
        pass

if __name__=='__main__':
    #Test/example program, don't modify
    l1=[1, 1, 1, 1]
    l2=[-2, 2, 3, -3]
    l3=[-1, 2, -2, 0]
    
    v1=Vect(l1)
    v2=Vect(l2)
    v3=Vect(l3)

    #Testataan pistetulo
    delta=0.01
    assert abs(v1@v2-0)<delta
    assert abs(v1@v1-4)<delta
    assert abs(v2@v2-26)<delta
    assert abs(v3@v2-0)<delta
    assert abs(v3@v1-(-1))<delta


