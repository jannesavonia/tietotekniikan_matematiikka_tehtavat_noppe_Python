import unittest
from helpers import *
import pandas as pd
import numpy as np
#from pandashelper import *
#import timeout_decorator

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


def accurateP(t):
    return 1/(1+np.exp(-t))



class TestCode(unittest.TestCase):
    def test_PythonFunction(self):
        #Test python function (in this case function name is combine)
        #Test code (my_code) must be implemented
        rmoutput()
        self.startTest()

        ret=callmain(input='', timeout=5)
        #print(ret)

        df=pd.read_csv('src/output.txt', names=['t', 'P'], header=None, dtype={'t':float, 'P':float}, sep=' ')

        self.assertEqual(len(df), 11, 'Data amount error')

        eps=0.00001
        for t in range(10):
            row=df[df['t']==t]
            P_data=row['P'].item()
            P_accurate=accurateP(t)
            self.assertTrue(np.abs(P_data-P_accurate)<=eps, 'Accuracy error!')
        
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

