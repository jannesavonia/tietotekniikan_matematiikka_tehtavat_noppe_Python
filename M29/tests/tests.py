import unittest
from helpers import *
import pandas as pd
import numpy as np
#import timeout_decorator
#from pandashelper import *
import numpy as np

#Never do following! The test process can be halted by student code!
#from my_code import *

def rmoutput():
    for filename in ['src/output.txt']:
        try:
            os.remove(filename)
            print(f'Removed {filename}')
        except:
            pass


started_tests = 0
completed_tests = 0


def heigh_accurate(t):
    thrust_t=1.0
    fall_t=1.0
    cycle_t=thrust_t+fall_t
    cycles=int(t//cycle_t)
    lastcycle_t=t%cycle_t
    last_thrust_t=np.min([lastcycle_t, thrust_t])
    last_fall_t=np.max([lastcycle_t-thrust_t, 0.0])

    g=-10
    F=2000
    m=100

    a_thrust=F/m+g
    a_fall=g

    v=0
    h=0
    for i in range(cycles):
        v0=v
        v+=thrust_t*a_thrust
        h+=v0*thrust_t+0.5*a_thrust*(thrust_t**2)

        v0=v
        v+=fall_t*a_fall
        h+=v0*fall_t+0.5*a_fall*(fall_t**2)

    v0=v
    v+=last_thrust_t*a_thrust
    h+=v0*last_thrust_t+0.5*a_thrust*(last_thrust_t**2)

    v0=v
    v+=last_fall_t*a_fall
    h+=v0*last_fall_t+0.5*a_fall*(last_fall_t**2)

    return h


class TestCode(unittest.TestCase):
    def test_PythonFunction(self):
        #Test python function (in this case function name is combine)
        #Test code (my_code) must be implemented
        rmoutput()
        self.startTest()

        ret=callmain(input='', timeout=5)
        #print(ret)

        df=pd.read_csv('src/output.txt', names=['t', 'x'], header=None, dtype={'t':float, 'x':float}, sep=' ')

        self.assertEqual(len(df), 11, 'Data amount error')

        eps=0.15
        for t in range(10):
            row=df[df['t']==t]
            h_data=row['x'].item()
            h_accurate=heigh_accurate(t)
            self.assertTrue(np.abs(h_data-h_accurate)<=eps, 'Accuracy error!')
        
        self.endTest()

    def startTest(self):
        global started_tests
        started_tests=started_tests+1
        print('\nStart test', started_tests)
        rmoutput()

    def endTest(self):
        global completed_tests
        print('End test', started_tests)
        completed_tests=completed_tests+1
        rmoutput()


def completed():
    global completed_tests
    return completed_tests

def started():
    global started_tests
    return started_tests

