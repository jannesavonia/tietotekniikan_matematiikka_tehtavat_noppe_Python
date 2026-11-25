"""
M12

Toteuta RSA-salauksen salaus- ja purkufunktio alle. Avaimet ovat Kpub=(n, e)
ja Kpriv=(n, d), jossa n, e, d ovat kokonaislukuja, sekä M<n ja C<N 
kokonaislukuja.

Jos käytät aiempien tehtävien ratkaisuja, niin kopioi lähdekoodit tähän 
tiedostoon. Älä koeta käyttää niitä moduleina.
"""


def E(Kpub, M):
    
    return C



def D(Kpriv, C):
    
    return M

if __name__=="__main__":
    Kpub=(221, 7)
    Kpriv=(221, 55)
    M=197
    C=E(Kpub, M)
    assert C==141
    Mreceived=D(Kpriv, C)
    assert Mreceived==M

    Kpub=(76147843, 17)
    Kpriv=(76147843, 17912753)
    M=2525417
    C=E(Kpub, M)
    assert C==66511275
    Mreceived=D(Kpriv, C)
    assert Mreceived==M
    