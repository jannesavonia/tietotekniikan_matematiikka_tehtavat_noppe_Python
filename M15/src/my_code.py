"""
M03

Lisää Vect-luokkaan vektorin normin palauttava metodi norm(). Katso esimerkki
tarvittaessa testiohjelmasta.

Lisää myös luokkametodi dist(a, b), joka palauttaa
pisteiden a ja b välisen etäisyyden. a ja b ovat pisteiden paikkavaktoreita. 
Katso esimerkki tarvittaessa testiohjelmasta.

Kopioi edellisen tehtävän Vect-luokka tähän pohjaksi.

"""

import math

class Vect:
    #Kopioi Vect luokka tähän
    
    def norm(self):
        pass

    def dist(a, b):
        pass

if __name__=='__main__':
    #Test/example program, don't modify
    l1=[1, 1, 1, 1]
    l2=[0.3, 0.4]
    a=3.1
    b=-0.7
    
    v1=Vect(l1)
    v2=Vect(l2)

    len1=2.0
    a_len1=abs(a)*len1
    len2=0.5
    b_len2=abs(b)*len2

    delta=0.01

    #Normin laskenta
    norm_v1=v1.norm()
    assert abs(len1-norm_v1)<delta
    assert abs(a_len1-(a*v1).norm())<delta
    assert abs(len2-v2.norm())<delta
    assert abs(b_len2-(b*v2).norm())<delta

    l1=[0.5, 0.1]
    l2=[0.3, 0.4]

    p1=Vect(l1)
    p2=Vect(l2)

    d=0.13

    delta=0.01
    #p1 ja p2 etäisyys
    d_p1_p2=Vect.dist(p1, p2)
    assert abs(d_p1_p2-math.sqrt(d))<delta
