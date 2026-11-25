"""
M03

Toteuta alla oleviin funktiopohjiin substituutiosalaus. Modulin
pääohjelmaan on toteutettu testi, jonka avulla voit testata
ja suunnitella toteutustasi.

1) Salaamaton viesti sisältää kirjaimia a-z tai A-Z sekä välilyöntejä
   ja muita erikoismerkkejä
2) Kaikki kirjaimet muutetaan isoiksi kirjaimiksi ennen salausta
3) Välilyönnit ja erikoismerkit jätetään sellaisenaan salattuun viestiin
4) Oikealla avaimella purettu viesti on identtinen alkuperäisen
   salaamattoman viestin kanssa, lukuun ottamatta sitä, että kaikki
   kirjaimet ovat muuttuneet isoiksi.
5) Avain on sanakirja (dict), jonka avain kuvautuu salauksessa vastaavaksi arvoksi.
   Esimerkiksi alla olevassa avaimessa A kuvautuu K:ksi ja D kuvautuu L:ksi.
   Purettaessa salausta tapahtuu tietenkin päinvastainen, eli K kuvautuu A:ksi ja
   L kuvautuu D:ksi. 
"""

def E(K, M):
    #Your code here

    return C

def D(K, C):
    #Your code here
    
    return M

if __name__=="__main__":
    M='Et osaa murtaa tata!'
    K={
        'A': 'K',
        'B': 'B',
        'C': 'N',
        'D': 'L',
        'E': 'M',
        'F': 'A',
        'G': 'O',
        'H': 'F',
        'I': 'G',
        'J': 'H',
        'K': 'W',
        'L': 'X',
        'M': 'Y',
        'N': 'Z',
        'O': 'P',
        'P': 'Q',
        'Q': 'T',
        'R': 'U',
        'S': 'R',
        'T': 'E',
        'U': 'S',
        'V': 'V',
        'W': 'C',
        'X': 'I',
        'Y': 'D',
        'Z': 'J'
    }
    print(f'M = "{M}"')
    print(f'K = {K}')

    C=E(K, M)
    print(f'C = "{C}"')
    
    M_received=D(K, C)
    print(f'M_received = "{M_received}"')

    assert C=='ME PRKK YSUEKK EKEK!'
    assert M_received==M.upper()
