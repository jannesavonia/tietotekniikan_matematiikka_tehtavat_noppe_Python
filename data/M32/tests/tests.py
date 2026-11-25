import unittest
from helpers import *
import numpy as np
import pandas as pd 
import random as rnd
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

class TestCode(unittest.TestCase):
    def test_PythonFunction(self):
        #Test python function (in this case function name is combine)
        #Test code (my_code) must be implemented
        w=np.sqrt(3/2)

        rmoutput()
        self.startTest()

        ret=callmain(input='', timeout=5)
        eps=0.01

        #data=read_csv('src/output.txt', columns={'t':Float,'x':Float})
        data=pd.read_csv('src/output.txt', names=['t', 'x'], header=None, dtype={'t':float, 'x':float}, sep=' ')
        self.assertTrue(np.abs(data['x'].min()+0.5)<eps, "Too small x-value found")
        self.assertTrue(np.abs(data['x'].max()-0.5)<eps, "Too large x-value found")
        self.assertTrue(data['t'].min()>-eps, "Too small t-value found")
        self.assertTrue(data['x'].max()-100<eps, "Too large t-value found")
        self.assertEqual(len(data), 101, 'Wrong number of rows in output.txt')

        self.assertTrue(np.abs(0.4936565101919087-data['x'].iloc[5])<eps, 'Failure x-value')
        self.assertTrue(np.abs(0.4181577893614927-data['x'].iloc[97])<eps, 'Failure x-value')
        self.assertTrue(np.abs((-0.24067578761621775)-data['x'].iloc[65])<eps, 'Failure x-value')
        self.assertTrue(np.abs(0.12087357039839025-data['x'].iloc[81])<eps, 'Failure x-value')

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

