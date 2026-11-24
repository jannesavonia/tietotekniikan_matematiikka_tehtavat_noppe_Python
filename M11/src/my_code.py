"""
M11

Toteuta funktio keys(p, q, e), joka palauttaa julkisen ja yksityisen avaimen
RSA-salaukseen.

Palautetut avaimet ovat Kpub=(n, e) ja Kpriv=(n, d), jossa n, e, d ovat kokonaislukuja.

Jos käytät aiempien tehtävien ratkaisuja, niin kopio lähdekoodit tähän 
tiedostoon. Älä koeta käyttää niin moduleina.
 
"""


def keys(p, q, e):
    pass

        
if __name__=="__main__":
    Kpub, Kpriv=keys(17, 13, 7)
    #print(Kpub, Kpriv)
    assert Kpub==(221, 7)
    assert Kpriv==(221, 55)

    try:
        Kpub, Kpriv=keys(17, 13, 3)
        assert False, 'syt((13-1)*(17-1), 3)=3, exception not generated'
    except:
        pass

    Kpub, Kpriv=keys(12601, 6043, 17)
    #print(Kpub, Kpriv)
    assert Kpub==(76147843, 17)
    assert Kpriv==(76147843, 17912753)
    
