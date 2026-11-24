"""
M09

Toteuta alla olevaan pohjaan modulaariaritmetiikan toteuttava luokka

1) +,-,* operaattorit toimivat myös kun oikealla puolella on kokonaisluku
2) Osa koodista on valmiiksi kirjoitettu, älä muokkaa sitä
3) Toteuta luokka niin, etta luvun a mod n a:lle pätee 0<=a<n.
"""

class Mod:
    def __init__(self, a, n):
        self.n=n
        self.a=a%n

    #Malliksi toteutettu +
    def __add__(self, b):
        if type(b) is int:
            return Mod(self.a+b, self.n)
        else:
            if self.n!=b.n:
                raise ValueError
            return Mod(self.a+b.a, self.n)

    def __sub__(self, b):
        pass

    def __mul__(self, b):
        pass

    def __eq__(self, b):
        pass

    #Malliksi toteutettu str()
    def __str__(self):
        return f'({self.a} mod {self.n})'

    #Malliksi toteutettu int()
    def __int__(self):
        return self.a

    def __pow__(self, k):
        #Ala laske potenssiin korotusta kokonaisluvulla:
        #return Mod(self.a**k, self.n)
        #
        #Käytä pow(a, k, n)-funktiota.

        
if __name__=='__main__':
    a_1_6=Mod(1, 6)
    a_17_6=Mod(17, 6)
    b_1_5=Mod(1, 5)
    b_11_5=Mod(11, 5)

    #Test exception if a.n!=b.n
    error=None
    try:
        c=a_1_6+b_1_5
        error='No exception with Mod(1,5)+Mod(1,6)'
    except:
        pass
    assert error==None, error
    
    try:
        c=a_1_6-b_1_5
        error='No exception with Mod(1,5)-Mod(1,6)'
    except:
        pass
    assert error==None, error

    try:
        c=a_1_6*b_1_5
        error='No exception with Mod(1,5)*Mod(1,6)'
    except:
        pass
    assert error==None, error

    try:
        c=a_1_6**(-1)
        error='No exception with Mod(1,6)**(-1)'
    except:
        pass
    assert error==None, error

    try:
        c=a_1_6**1.1
        error='No exception with Mod(1,6)**1.2'
    except:
        pass
    assert error==None, error

    

    #Test __add__(self, b) and __str__(self)    
    assert str(a_1_6+a_17_6)=='(0 mod 6)', '(1 mod 6)+(17 mod 6) != (0 mod 6)' 
    assert str(b_1_5+b_11_5)=='(2 mod 5)', '(1 mod 5)+(11 mod 5) != (2 mod 5)'

    #Test __mul__(self, b) __sub__(self, b), and __eq__(self, b)
    d_6=a_17_6*5
    assert d_6==Mod(1, 6)

    d_6=(a_17_6+a_1_6)*a_17_6
    assert d_6==Mod(0, 6)

    d_6=(a_17_6-a_1_6)*a_17_6
    assert d_6==Mod(2, 6)

    d_5=b_11_5**4
    assert d_5==Mod(1, 5)

    d_5=(b_1_5+b_11_5)**5
    assert d_5==Mod(2, 5)
    assert int(d_5)%5==2
    assert int(b_11_5)%5==1
