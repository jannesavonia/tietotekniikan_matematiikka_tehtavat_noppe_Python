"""
M10

Toteuta funktio syt_ext(a, b), joka palauttaa g, x, y, jossa 
g=syt(a, b) ja 
ax+by=syt(a, b) 
"""

def syt_ext(a, b):
    pass        

        
if __name__=="__main__":
    a, b=100, 35
    g, x, y=syt_ext(a, b)
    assert g==5
    assert a*x+b*y-g==0

    a, b=10, 35
    g, x, y=syt_ext(a, b)
    assert g==5
    assert a*x+b*y-g==0
    
    a, b=21, 14
    g, x, y=syt_ext(a, b)
    assert g==7
    assert a*x+b*y-g==0

    a, b=3, 21
    g, x, y=syt_ext(a, b)
    assert g==3
    assert a*x+b*y-g==0

    a, b=3, 3
    g, x, y=syt_ext(a, b)
    assert g==3
    assert a*x+b*y-g==0
    
    a, b=2, 62
    g, x, y=syt_ext(a, b)
    assert g==2
    assert a*x+b*y-g==0

    a, b=13, 17
    g, x, y=syt_ext(a, b)
    assert g==1
    assert a*x+b*y-g==0

    a, b=12378, 3054
    g, x, y=syt_ext(a, b)
    assert g==6
    assert a*x+b*y-g==0
