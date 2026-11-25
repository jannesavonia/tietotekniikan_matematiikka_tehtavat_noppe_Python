import unittest
from helpers import *
#import timeout_decorator
import numpy as np
import pandas as pd 
#from pandashelper import *


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
        rmoutput()
        self.startTest()

        py_code="""
import sys
import random as rnd
sys.path.insert(0, '../src')

import numpy as np
from my_code import solver

solver(20)

print('difhnisdhfnsduif')
"""

        cs_code="""
using System;
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;
using System.IO;
using MathNet.Numerics.Data.Text;

namespace Lineaarialgebra
{
    class TestProgram {
		static void Main() {
            MyProgram.solver(20);

            Console.WriteLine("difhnisdhfnsduif");
		}
    }
}
"""
        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=5)

        self.assertTrue('difhnisdhfnsduif' in ret, 'Test failed, unknown error!')

        try:
            
            data=pd.read_csv('src/output.txt', names=['t', 'x', 'y'], header=None, dtype={'t':float, 'x':float, 'y':float}, sep=' ')
            #data=read_csv('src/output.txt', columns={'t': Float,'x': Float,'y': Float})
            #data=pd.read_csv('src/output.txt', delimiter=' ', names=['t','x','y'])
        except:
            self.assertTrue(False, 'Reading src/output.txt failed!')

        eps=0.01
        self.assertEqual(len(data), 21, 'Expected 21 rows')
        for idx, row in data.iterrows():
            t=row['t']
            x_correct=2.0*np.cos(t)
            y_correct=2.0*np.sin(t)
            x_computed=row['x']
            y_computed=row['y']
            
            self.assertLessEqual(abs(idx-t), 0.001, f't should be saved on integer t. idx={idx}, t={row["t"]}')
            diff=np.array([x_computed-x_correct, y_computed-y_correct])
            diff_norm=np.linalg.norm(diff)
            print(t, x_correct, x_computed, y_correct, y_computed, diff, diff_norm)
            self.assertLessEqual(diff_norm, eps, 'Accuracy error')

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

