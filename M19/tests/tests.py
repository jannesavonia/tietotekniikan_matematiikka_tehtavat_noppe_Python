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
from my_code import perpendicular

v1=np.array([1, 0, 0], dtype=np.double)
v2=np.array([0, 1, 0], dtype=np.double)
v3=np.array([0, 0, 1], dtype=np.double)

assert perpendicular(v1, v2)
assert perpendicular(v1, v3)
assert perpendicular(v3, v2)
assert perpendicular(-v1, v2)
assert perpendicular(v1, -v3)
assert perpendicular(v3, -v2)
print('coord_axis test completed')

v1=np.array([1, 2, 3], dtype=np.double)
v2=np.array([-3, 0, 1], dtype=np.double)
v3=np.array([0, 1, 0], dtype=np.double)

assert perpendicular(v1, v2)
assert perpendicular(v2, v3)
assert perpendicular(v1, -v2)
assert perpendicular(-v2, v3)
assert perpendicular(-v1, -v2)
assert perpendicular(-v2, -v3)
print('positive_perpendicular test completed')

v4=np.array([1, -1, 2], dtype=np.double)
assert not perpendicular(v1, v3)
assert not perpendicular(v1, v4)
assert not perpendicular(v3, v4)
assert not perpendicular(-v1, v3)
assert not perpendicular(v1, -v4)
assert not perpendicular(-v3, v4)
print('negative_perpendicular test completed')

print('892349898')
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
        static int Main(string[] args)
        {
            Vector<double> v1=CreateVector.Dense(new double[] {1, 0, 0});
    		Vector<double> v2=CreateVector.Dense(new double[] {0, 1, 0});
    		Vector<double> v3=CreateVector.Dense(new double[] {0, 0, 1});

            Trace.Assert(MyProgram.perpendicular(v1, v2));
            Trace.Assert(MyProgram.perpendicular(v1, v3));
            Trace.Assert(MyProgram.perpendicular(v3, v2));
            Trace.Assert(MyProgram.perpendicular(-v1, v2));
            Trace.Assert(MyProgram.perpendicular(v1, -v3));
            Trace.Assert(MyProgram.perpendicular(v3, -v2));
            Console.WriteLine("coord_axis test completed");

    		v1=CreateVector.Dense(new double[] {1, 2, 3});
    		v2=CreateVector.Dense(new double[] {-3, 0, 1});
    		v3=CreateVector.Dense(new double[] {0, 1, 0});

            Trace.Assert(MyProgram.perpendicular(v1, v2));
            Trace.Assert(MyProgram.perpendicular(v2, v3));
            Trace.Assert(MyProgram.perpendicular(v1, -v2));
            Trace.Assert(MyProgram.perpendicular(-v2, v3));
            Trace.Assert(MyProgram.perpendicular(-v1, -v2));
            Trace.Assert(MyProgram.perpendicular(-v2, -v3));
            Console.WriteLine("positive_perpendicular test completed");

            Vector<double> v4=CreateVector.Dense(new double[] {1, -1, 2});
            Trace.Assert(!MyProgram.perpendicular(v1, v3));
            Trace.Assert(!MyProgram.perpendicular(v1, v4));
            Trace.Assert(!MyProgram.perpendicular(v3, v4));
            Trace.Assert(!MyProgram.perpendicular(-v1, v3));
            Trace.Assert(!MyProgram.perpendicular(v1, -v4));
            Trace.Assert(!MyProgram.perpendicular(-v3, v4));
            Console.WriteLine("negative_perpendicular test completed");

            Console.WriteLine("892349898");
            return 0;
        }
    }
}
"""
        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=5)
        print(ret)
        
        self.assertTrue('coord_axis test completed' in ret, 'ERROR: Coordinate axis are perpendicular!')
        self.assertTrue('positive_perpendicular test completed' in ret, 'ERROR: False negative!')
        self.assertTrue('negative_perpendicular test completed' in ret, 'ERROR: False positive!')

        self.assertTrue('892349898' in ret, 'Test failed, unknown error!')
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

