import unittest
from helpers import *
#import timeout_decorator
import pandas as pd
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

from my_code import euler_circle


T=19
dt=0.01
N=int(T/dt)
euler_circle(dt, N)

print('y98y89b89yf')
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
			double T=19;
    		double dt=0.01;
            int N=Convert.ToInt32(T/dt);
            MyProgram.euler_circle(dt, N, "output.txt");

            Console.WriteLine("y98y89b89yf");
		}
    }
}
"""
        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=5)

        self.assertTrue('y98y89b89yf' in ret, 'Test failed, unknown error!')

        expected_data_error={
            0.66: (0.7869283973051523, 0.612061703815305),
            8.76: (-0.7901233068802996, 0.6079439815238961),
            12.99: (0.9095483879124364, 0.41062630152158164)
        }

        expected_data_real={
            0.66: (0.7930595658248866, 0.6141617815003314),
            8.76: (-0.7839544629690068, 0.6258145192946445),
            12.99: (0.9136591050333192, 0.4115102714230574)
        }


        data=pd.read_csv('src/output.txt', names=['t', 'x', 'y'], header=None, dtype={'t':float, 'x':float, 'y':float}, sep=' ')

        eps=0.001
        dt=0.01
        def compare_xy(data, t, x, y):
            d=data.loc[(t-dt/2<data['t']) & (data['t']<t+dt/2)]
            #data_x=float(d['x'])
            #data_y=float(d['y'])
            data_x=float(d['x'].iloc[0])
            data_y=float(d['y'].iloc[0])
        
            return abs(data_x-x), abs(data_y-y)

        try:
            for t, (x, y) in expected_data_error.items():
                #d=data.loc[(t-dt/2<data['t']) & (data['t']<t+dt/2)]
                #data_x=float(d['x'].iloc[0])
                #data_y=float(d['y'].iloc[0])
                #print(t, x, y, data_x, data_y)
                dx,dy=compare_xy(data, t, x, y)
                self.assertLessEqual(dx, eps, "Not expected result")
                self.assertLessEqual(dy, eps, "Not expected result")
        except Exception as e:        
            for t, (x, y) in expected_data_real.items():
                #d=data.loc[(t-dt/2<data['t']) & (data['t']<t+dt/2)]
                #data_x=float(d['x'].iloc[0])
                #data_y=float(d['y'].iloc[0])
                #print(t, x, y, data_x, data_y)
                dx,dy=compare_xy(data, t, x, y)
                self.assertLessEqual(dx, eps, "Not expected result")
                self.assertLessEqual(dy, eps, "Not expected result")

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

