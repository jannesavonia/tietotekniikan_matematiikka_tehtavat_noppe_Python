"""
M02

Laajenna Vect-luokkaa siten että vektorin voi kertoa liukuluvulla. Katso esimerkki
tarvittaessa testiohjelmasta.

Kopioi edellisen tehtävän Vect-luokka tähän pohjaksi.

"""

class Vect:
    #Your Vect code here

    def __rmul__(self, a):
        pass


if __name__=='__main__':
    #Test/example program, don't modify
    l1=[-0.5, 1]
    l2=[-1.5, 0.8]
    a=3.1
    b=-0.7
    
    v1=Vect(l1)
    v2=Vect(l2)

    #Kertolaskuesimerkki
    a_times_v1=a*v1
    b_times_v2=b*v2

    print(f'{a}*{v1}={a_times_v1}')
    print(f'{b}*{v2}={b_times_v2}')

    #Test +, -, and []
    delta=0.01
    for i, _ in enumerate(l1):
        assert abs(a*l1[i]-a_times_v1[i])<delta
        assert abs(b*l2[i]-b_times_v2[i])<delta