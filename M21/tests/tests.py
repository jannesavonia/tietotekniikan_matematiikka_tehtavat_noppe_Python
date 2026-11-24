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
from my_code import T, S

import random as rnd 
epsilon=0.01

for i in range(100):
    x=np.array([rnd.gauss(1, 5), 1])
    x_real=x[0]
    for _ in range(10):
        c=rnd.gauss(1, 5)
        dx=rnd.gauss(1, 2)
        x=T(dx)@x
        x=S(c)@x
        x_real=x_real+dx
        x_real=x_real*c

    if np.abs(x[0]-x_real)>epsilon:
        print('ERROR: Transform failed')
        
print('2sd4873264nsns')
"""

        cs_code="""
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;

namespace Lineaarialgebra
{
    class MyTestProgram
    {
        static double epsilon=0.01;

        static int Main(string[] args)
        {
            Random rnd=new Random();

			for(int i=0; i<100; i++) {
				Vector<double> x=CreateVector.Dense(new double[] {rnd.NextDouble(), 1});
				double x_real=x[0];
				for(int j=0; j<10; j++) {
					double c=1+5*rnd.NextDouble();
					double dx=1+2*rnd.NextDouble();
					x=MyProgram.T(dx)*x;
					x=MyProgram.S(c)*x;
					x_real+=dx;
					x_real*=c;
				}
				if(Math.Abs(x_real-x[0])>epsilon) {
                    Console.WriteLine("ERROR: Transform failed");
                }
            }

            Console.WriteLine("2sd4873264nsns");
            return 0;
        }
    }
}
"""
        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=5)
        print(ret)
        
        self.assertTrue('ERROR: Transform failed' not in ret, 'ERROR: Transform failed')

        self.assertTrue('2sd4873264nsns' in ret, 'Test failed, unknown error!')
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

