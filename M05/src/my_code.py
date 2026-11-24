"""
M05

Toteuta alla oleviin funktiopohjiin transpositiosalaus. Modulin
pääohjelmaan on toteutettu testi, jonka avulla voit testata
ja suunnitella toteutustasi.

1) Salaamaton viesti voi sisältää mitä tahansa merkkejä
2) Viestiä ei esikäsitellä millään tavoin ennen salausta
3) Salaus lisää alkuperäisen viestin loppuun tarvittavan määrän välilyöntejä
4) Oikealla avaimella purettu viesti on identtinen alkuperäisen
   salaamattoman viestin kanssa lukuun ottamatta edellä loppuun lisättyjä
   välilyöntejä
5) Avain on tuple, kuten luentokalvoissa on esitetty
"""

def E(K, M):
    #Your code here    
    return C

def D(K, C):
    #Your code here    
    return M


#Test software, don't modify
if __name__=="__main__":
    M='tama viesti on salattu transpositiosalauksella'
    K=(3, 6, 7, 4, 2, 1, 5)
    print(f'M = "{M}"')
    print(f'K = {K}')

    C=E(K, M)
    print(f'C = "{C}"')
    
    M_received=D(K, C)
    print(f'M_received = "{M_received}"')

    assert C=="v taiamo einstta ltsanaurs titpiooskusasal  ea ll"
    lM=len(M)
    assert M_received[:lM]==M
