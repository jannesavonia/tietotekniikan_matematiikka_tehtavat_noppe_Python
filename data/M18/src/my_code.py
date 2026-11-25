"""
M18

Lisää Vect-luokkaan projektion laskeva funktio proj(v), joka
laskee vektorin projektion v:lle. Jos dimensiot eivät täsmää,
niin heitetään poikkeus.

Kopioi edellisen tehtävän Vect-luokka tähän pohjaksi.

"""

import math

class Vect:
    #Kopioi koodi tähän

    def proj(self, v):
        #Your code here

if __name__=='__main__':
    #Test/example program, don't modify
    l1=[1, 1, 1, 1]
    l2=[1, 2, 1, -3]
    l3=[-4, 2, -2, 0]
    
    v1=Vect(l1)
    v2=Vect(l2)
    v3=Vect(l3)

    delta=0.01
    #Lasketaan projektioita
    p_v2_v1=v2.proj(v1) #v2 projektio v1:lle
    p_v2_v3=v2.proj(v3)
    p_v1_v3=v1.proj(v3)

    #Testataan, että projektiot ovat oikein
    assert ((v1@v1)*p_v2_v1-(v1@v2)*v1).norm()<delta
    assert ((v3@v3)*p_v2_v3-(v3@v2)*v3).norm()<delta
    assert ((v3@v3)*p_v1_v3-(v3@v1)*v3).norm()<delta

