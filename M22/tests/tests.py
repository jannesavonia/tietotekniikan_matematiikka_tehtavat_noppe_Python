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
from my_code import unitnormal

epsilon=0.0001

for i in range(100):
        a=np.random.randn(3)
        b=np.random.randn(3)
        if np.linalg.norm(a)<epsilon or np.linalg.norm(b)<epsilon:
            continue

        normal=unitnormal(a, b)
        minus_normal=unitnormal(b, a)
        assert np.linalg.norm(normal+minus_normal)<epsilon, 'ERROR:axb!=-bxa'
        assert np.abs(a@normal)<epsilon, 'ERROR: perpendocularity failed'
        assert np.abs(b@normal)<epsilon, 'ERROR: perpendocularity failed'
        assert np.abs(np.linalg.norm(normal)-1)<epsilon, 'ERROR: not unit vector'

print('2sd4873264nsns')
"""
        cs_code="""
using System;
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;
//using MathNet.Spatial.Euclidean;

namespace Lineaarialgebra
{
    class MyTestProgram {
		static void Main() {
			double epsilon=0.0001;
			Random rnd=new Random();

			for(int i=0; i<100; i++) {
				Vector<double> a=CreateVector.Dense(new double[] {rnd.NextDouble(), rnd.NextDouble(), rnd.NextDouble()});
				Vector<double> b=CreateVector.Dense(new double[] {rnd.NextDouble(), rnd.NextDouble(), rnd.NextDouble()});

				if(a.L2Norm()<epsilon || b.L2Norm()<epsilon) {
					continue;
				}

				Vector<double> normal=MyProgram.unitnormal(a, b);
				Vector<double> minus_normal=MyProgram.unitnormal(b, a);

				//Check that a x b = -b x a
                if((normal+minus_normal).L2Norm()>=epsilon) {
                    Console.WriteLine("ERROR:axb!=-bxa");
                    return;
                }
                if(Math.Abs(a*normal)>=epsilon) {
                    Console.WriteLine("ERROR: perpendocularity failed");
                    return;
                }
                if(Math.Abs(b*normal)>=epsilon) {
                    Console.WriteLine("ERROR: perpendocularity failed");
                    return;
                }
                if(Math.Abs(normal.L2Norm()-1)>=epsilon) {
                    Console.WriteLine("ERROR: not unit vector");
                    return;
                }
			}
            Console.WriteLine("2sd4873264nsns");
		}
    }
}
"""

        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=5)
        print(ret)
        
        self.assertTrue('ERROR:axb!=-bxa' not in ret, 'ERROR:axb!=-bxa')
        self.assertTrue('ERROR: perpendocularity failed' not in ret, 'ERROR: return vector not perpendicular to a or b')
        self.assertTrue('ERROR: not unit vector' not in ret, 'ERROR: result not unit vector')

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

