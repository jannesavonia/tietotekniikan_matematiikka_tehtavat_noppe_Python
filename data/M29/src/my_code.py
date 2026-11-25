"""
M29
Raketin massa on 100kg ja sen moottorin työntövoima on 2000N. Oletetaan, että
alkunopeus ja -paikka ovat molemmat 0. Raketti ammuttaan suoraan ylöspäin siten,
että moottori on aluksi päällä 1s ja sitten pois päältä saman ajan käynnistyen taas 1s
ajaksi jne. 

Kirjoita ohjelma, joka simuloi raketin lentokorkeutta ajan funktiona. Ohjelma tallentaa
tiedostoon output.txt raketin korkeuden ajanhetkinä t=0, 1, 2...10 (sekuntia). Tiedoston 
ensimmäinen sarake sisältää ajan (sekunteina) ja toinen korkeuden (metreinä).
Yksiköitä ei talleteta tiedostoon. Sarakkeet erotetaan välilyönnillä. Käytä 
gravitaatiokiihtyvyydelle arvoa g=10m/s^2 ja jätetään ilmanvastus huomioimatta.

Valitse tehtävään sopiva menetelmä. Raketin korkeus millä tahansa ajanhetkellä
saa erota todellisesta arvosta enintään 0.1m.
"""

import os
import numpy as np 

filename=os.path.dirname(__file__)+'/output.txt'

def save(outf, x, t):
    outf.write(f'{int(t)} {x}\n')


#Your code here. Create a software, not a single function

#Test code 
import pandas as pd

data=pd.read_csv(filename, delimiter=' ', names=['t','x'])

print(data)

assert len(data)==11, 'Length of data error'
assert np.abs(data[data['t']==0]['x'].item()-0.0)<=0.1, 'Accuracy error'
assert np.abs(data[data['t']==1]['x'].item()-5.0)<=0.1, 'Accuracy error'
assert np.abs(data[data['t']==10]['x'].item()-50.0)<=0.1, 'Accuracy error'

