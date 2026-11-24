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
sys.path.insert(0, '../src')

import numpy as np
from my_code import direction

epsilon=0.0001

for i in range(100):
    a=np.random.randn(3)
    a=np.append(a, [1])
    b=np.random.randn(3)
    b=np.append(b, [1])
    if np.linalg.norm(a-b)<epsilon:
        continue

    x=direction(a,b)
    z=a-b
    if abs(z@x+np.linalg.norm(z))>=epsilon:
        print('ERROR: not unit direction')

print('2sd487sas3264ns')
"""

        cs_code="""
using System;
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;

namespace Lineaarialgebra
{
    class TestProgram {
		static double epsilon=0.0001;

		static void Main() {
			Random rnd=new Random();

			for(int i=0; i<100; i++) {
				double[] lx=new double[4];
				double[] ly=new double[4];

				for(int j=0; j<3; j++) {
					lx[j]=2*rnd.NextDouble()-1.0;
					ly[j]=2*rnd.NextDouble()-1.0;
				}
				lx[3]=1;
				ly[3]=1;

				Vector<double> a=CreateVector.Dense(lx);
				Vector<double> b=CreateVector.Dense(ly);

				if((a-b).L2Norm()<epsilon) {
					continue;
				}

				Vector<double> x=MyProgram.direction(a, b);
				Vector<double> z=a-b;
                if(Math.Abs(z*x+z.L2Norm())>epsilon) {
                    Console.WriteLine("ERROR: not unit direction");
                }
			}
            Console.WriteLine("2sd487sas3264ns");
		}
    }
}
"""
        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=5)
        #print(ret)
        
        self.assertTrue('ERROR: not unit direction' not in ret, 'ERROR: not unit direction vector')

        self.assertTrue('2sd487sas3264ns' in ret, 'Test failed, unknown error!')
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

