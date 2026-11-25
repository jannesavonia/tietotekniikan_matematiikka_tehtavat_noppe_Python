"""
M07

Toteuta funktio sieve(N), joka palauttaa joukon, jossa on alkuluvut <=N.

Vihje:
1) tee lista P, joka sisältää luvut 0..N
2) aseta poistetut numerot listassa 0:ksi
3) lopuksi muuta lista joukoksi P
4) poista joukosta P luvut 0 ja 1
"""

#Naita saatat tarvita 
from math import ceil, sqrt

def sieve(N):
    #Your code here
    return P

if __name__=="__main__":
    primes=sieve(1000000)
    assert len(primes)==78498
    assert 99391 in primes
    assert 999983 in primes
    assert 2 in primes
    assert 3 in primes
    assert 23 in primes
    assert 4 not in primes
    assert 99837 not in primes

