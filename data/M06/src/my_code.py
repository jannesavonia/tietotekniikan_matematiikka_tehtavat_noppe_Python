"""
M06

Toteuta funktio syt(a, b), joka palauttaa a:n ja b:n suurimman yhteisen tekijän. 
"""

def syt(a, b):
    pass
        
if __name__=="__main__":
    assert syt(100, 35)==5
    assert syt(35, 100)==5
    assert syt(10, 35)==5
    assert syt(21, 14)==7
    assert syt(3, 21)==3
    assert syt(3, 3)==3
    assert syt(2, 62)==2
    assert syt(13, 17)==1
    assert syt(12378, 3054)==6
