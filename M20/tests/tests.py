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
from my_code import projection

epsilon=0.0001

def check(x, y):
    proj=projection(x, y)
    perpendicular=(np.abs((x-proj)@y)<epsilon)
    if not perpendicular:
        print('ERROR x-Px was not perpendicular to y')
    same_dir=np.abs(np.abs(y@proj)-(np.linalg.norm(y)*np.linalg.norm(proj)))<epsilon
    if not same_dir:
        print('ERROR ||Px|| was not correct, or Px was not parallel to y')
    return perpendicular, same_dir

for i in range(3, 30):
    print(32*'-')
    x=np.random.randn(i)
    y=np.random.randn(i)
    print(f'x={x}')
    print(f'y={y}')
    perp, dir=check(x, y)
    assert perp
    assert dir

print('2834873264')
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
        static double epsilon=0.0001;

    	public static void check(Vector<double> x, Vector<double> y, ref bool perp, ref bool dir) {
            Vector<double> proj=MyProgram.projection(x, y);
            perp=(Math.Abs((x-proj)*y)<epsilon);
            if(!perp) {
                Console.WriteLine("ERROR x-Px was not perpendicular to y");
            }
            dir=(Math.Abs(Math.Abs(y*proj)-(y.L2Norm()*proj.L2Norm()))<epsilon);
            if(!dir) {
                Console.WriteLine("ERROR ||Px|| was not correct, or Px was not parallel to y");
            }
		}

        static int Main(string[] args)
        {
            Random rnd=new Random();

            for(int i=3; i<30; i++) {
                Console.WriteLine("-------------------------------------------------");
                double[] lx=new double[i];
                double[] ly=new double[i];

                for(int j=0; j<i; j++) {
					lx[j]=2*rnd.NextDouble()-1.0;
					ly[j]=2*rnd.NextDouble()-1.0;
				}

				Vector<double> x=CreateVector.Dense(lx);
				Vector<double> y=CreateVector.Dense(ly);
				Console.WriteLine($"x={x}");
				Console.WriteLine($"y={y}");

				bool perp=false;
				bool dir=false;
				check(x, y, ref perp, ref dir);
                        if(!perp) {
                            Console.WriteLine("x-Px was not perpendicular to y");
                        }
        		Trace.Assert(perp); //'x-Px was not perpendicular to y'
        
                        if(!dir) {
                            Console.WriteLine("||Px|| was not correct, or Px was not parallel to y");
                        }
        		Trace.Assert(dir);  //'||Px|| was not correct, or Px was not parallel to y'

            }

            Console.WriteLine("2834873264");
            return 0;
        }
    }
}
"""
        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=5)
        print(ret)
        
        self.assertTrue('ERROR x-Px was not perpendicular to y' not in ret, 'ERROR x-Px was not perpendicular to y')
        self.assertTrue('ERROR ||Px|| was not correct, or Px was not parallel to y' not in ret, 'ERROR ||Px|| was not correct, or Px was not parallel to y')

        self.assertTrue('2834873264' in ret, 'Test failed, unknown error!')
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

