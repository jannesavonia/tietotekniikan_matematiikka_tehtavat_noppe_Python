"""
M01

Toteuta luokka Vect, joka osaa vektoreiden yhteen- ja vähennyslaskun.
Vektorin arvo annetaan muodostimen list-tyyppeisenä parametrina.
Mikäli laskutoimitusta yritetään vektoreille, joiden dimensio ei ole
sama, niin heitetään poikkeus. Lisäksi toteutetaan []-operaattori, joka palauttaa
vektorin alkion ja toimii kuten list-tyypin vastaava operaattori. Indeksointi alkaa 0:sta. 
Toteuta lisäksi str-operaattori, joka tulostaa vektorin muodossa [1, 2.3, 4, -1.2], siis
samoin kuin esimerkiksi Pythonin list-tyyppi.

Jotkin metodit on toteutettu valmiiksi. Voit toki muokata niitä jos on tarve.

"""

class Vect:
    def __init__(self, v):
        self.items=v.copy()

    def __add__(self, v):
        #Your code here

    def __sub__(self, v):
        #Your code here

    def __str__(self):
        return str(self.items)

    def __getitem__(self, i):
        return self.items[i]


if __name__=='__main__':
    #Test/example program, don't modify
    l1=[-0.5, 1]
    l2=[-1.5, -0.8]
    
    v1=Vect(l1)
    v2=Vect(l2)

    v1_plus_v2=v1+v2
    v1_minus_v2=v1-v2

    print(f'{v1}+{v2}={v1_plus_v2}')
    print(f'{v1}-{v2}={v1_minus_v2}')

    #Test +, -, and []
    delta=0.01
    for i, _ in enumerate(l1):
        assert abs(v1[i]+v2[i]-v1_plus_v2[i])<delta
        assert abs(v1[i]-v2[i]-v1_minus_v2[i])<delta
        assert abs(v1[i]-l1[i])<delta
        assert abs(v2[i]-l2[i])<delta

    #Test exception if adding mismatch vectors
    v3=Vect([1, 2, 3])
    try:
        v_error=v1+v3
        assert False, '__add__ dimension check failed'
    except:
        pass

    #Test exception if subtracting mismatch vectors
    try:
        v_error=v1-v3
        assert False, '__sub__ dimension check failed'
    except:
        pass
