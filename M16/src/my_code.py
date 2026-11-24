"""
M04

Lisää Vect-luokkaan funktio unit(), joka palauttaa vektorin kanssa
samansuuntaisen yksikkövektorin. Mikäli vektori on 0-vaktori,
niin heitetään poikkeus.

Kopioi edellisen tehtävän Vect-luokka tähän pohjaksi.

"""

import math

class Vect:
    #Kopioi Vect-luokka tänne
    
    def unit(self):
        pass

if __name__=='__main__':
    #Test/example program, don't modify
    l1=[1, 1, 1, 1]
    l2=[0.3, 0.4]
    a=3.1
    b=-0.7
    
    v1=Vect(l1)
    v2=Vect(l2)
    #Yksikkövektori
    u1=v1.unit()
    u2=v2.unit()

    delta=0.01
    norm_u1=u1.norm()
    norm_u2=u2.norm()

    #Testataan, että on yksikkövektori
    delta=0.01
    assert abs(1-norm_u1)<delta
    assert abs(1-norm_u2)<delta
    
    #Testataan, että saatu vektori on samansuuntainen kuin alkuperäinen vektori
    uu1=v1.norm()*u1
    assert((v1-uu1).norm()<delta)
    uu2=v2.norm()*u2
    assert((v2-uu2).norm()<delta)

    #Testataan, että 0-vaktori aiheuttaa poikkeuksen
    v0=Vect([0, 0, 0])
    try:
        u0=v0.unit()
        assert False, 'Exception failed'
    except:
        pass


