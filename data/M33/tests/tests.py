import unittest
from helpers import *
import numpy as np
import pandas as pd 
import random as rnd
#from matplotlib import pyplot as plt 

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
    def test_Python(self):
        #Test python function (in this case function name is combine)
        #Test code (my_code) must be implemented
        self.startTest()

        ret=callmain(input='', timeout=5).strip()
 
        self.assertEqual(ret, 'Olen antanut kurssipalautteen.')

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

