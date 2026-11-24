import unittest
from helpers import *
#import timeout_decorator

#Never do following! The test process can be halted by student code!
#from my_code import *

def rmoutput():
    for filename in []:
        try:
            os.remove(filename)
        except:
            pass


started_tests = 0
completed_tests = 0

class TestCode(unittest.TestCase):
    def test_PythonFunction(self):
        #Test python function (in this case function name is combine)
        #Test code (my_code) must be implemented
        self.startTest()

        py_code="""
import sys
import random as rnd
sys.path.insert(0, '../src')

import numpy as np
from my_code import move_rotate

epsilon=0.0001

for t in np.linspace(0, 10*np.pi, 1000):
    a=np.pi*t/16
    Z=move_rotate(t)
    if Z.shape!=(3, 3):
        print('ERROR: Matrix shape error')

    if abs(Z[0,0]+Z[2,0]+Z[0,1]-np.cos(a)+np.sin(a))>epsilon:
        print('ERROR: Angle error')
    
    if abs(Z[0,0]*Z[1,1]-Z[0,1]*Z[1,0]-1+Z[2,1])>epsilon:
        print('ERROR: Rotation part error')

    if abs(Z[2,0]+Z[0,2]+Z[1,2]+Z[2,2]+Z[2,1]-(1+np.cos(np.pi*t/10)*np.sin(np.pi*t)+np.cos(np.pi*t)))>epsilon:
        print('ERROR: Translation part error')


print('as8u98as98duasu')
"""
        cs_code="""
using System;
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;

namespace Lineaarialgebra
{
    class TestProgram {
		static void Main() {
    		double epsilon=0.0001;
			Random rnd=new Random();

			for(double t=0; t<10*Math.PI; t+=Math.PI/100) {
				double a=Math.PI*t/16;
				Matrix<double> Z=MyProgram.move_rotate(t);

                if(Z.ColumnCount!=3 || Z.RowCount!=3) {
                    Console.WriteLine("ERROR: Matrix shape error");
                }
                if(Math.Abs(Z[0,0]+Z[2,0]-Math.Cos(a))>epsilon) {
                    Console.WriteLine("ERROR: Angle error");
                }
                if(Math.Abs(Z[0,0]*Z[1,1]-Z[0,1]*Z[1,0]-1+Z[2,1])>epsilon) {
                    Console.WriteLine("ERROR: Rotation part error");
                }
				if(Math.Abs(Z[2,0]+Z[0,2]+Z[1,2]+Z[2,2]+Z[2,1]-(1+Math.Cos(Math.PI*t/10)*Math.Sin(Math.PI*t)+Math.Cos(Math.PI*t)))>epsilon) {
                    Console.WriteLine("ERROR: Translation part error");
                }
			}
            Console.WriteLine("as8u98as98duasu");
		}
    }
}
"""

        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=5)
        #print(ret)
        
        self.assertTrue('ERROR: Matrix shape error' not in ret, 'ERROR: Matrix shape error, must be 3x3')
        self.assertTrue('ERROR: Angle error' not in ret, 'ERROR: Angle error')
        self.assertTrue('ERROR: Rotation part error' not in ret, 'ERROR: Rotation part error')
        self.assertTrue('ERROR: Translation part error' not in ret, 'ERROR: Translation part error')

        self.assertTrue('as8u98as98duasu' in ret, 'Test failed, unknown error!')
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

