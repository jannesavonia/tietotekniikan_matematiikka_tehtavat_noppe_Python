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
import random as rnd
import sys
sys.path.insert(0, '../src')

from my_code import Vect

for n in range(1, 10):
    l1=[rnd.uniform(-10, 10) for i in range(n)]
    l2=[rnd.uniform(-10, 10) for i in range(n)]
    a=rnd.uniform(-10, 10)
    b=rnd.uniform(-10, 10)
    
    v1=Vect(l1)
    v2=Vect(l2)

    a_times_v1=a*v1
    b_times_v2=b*v2

    if type(a_times_v1) is Vect:
        print(f'return type passed, n={n}')

    delta=0.01
    for i, _ in enumerate(l1):
        assert abs(a*l1[i]-a_times_v1[i])<delta
        assert abs(b*l2[i]-b_times_v2[i])<delta

    print(f'* passed, n={n}')

print('89weyf98weyfy')
"""
        cs_code="""
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace Lineaarialgebra
{
    class MyTestProgram
    {
        static int Main(string[] args)
        {
            Random rnd=new Random();
        
            for(int n=1; n<10; n++) {
                var l1=new double[n];
                var l2=new double[n];
                var a=20.0*(rnd.NextDouble()-0.5);
                var b=20.0*(rnd.NextDouble()-0.5);

                for(int i=0; i<n; i++) {
                    l1[i]=20.0*(rnd.NextDouble()-0.5);
                    l2[i]=20.0*(rnd.NextDouble()-0.5);
                }

                var v1=new Vect(l1);
                var v2=new Vect(l2);

                Vect a_times_v1=a*v1;
                Vect b_times_v2=b*v2;
                Console.WriteLine($"return type passed, n={n}");

                double delta=0.01;

                for(int i=0; i<n; i++) {
                    Trace.Assert(Math.Abs(a*l1[i]-a_times_v1[i])<delta);
                    Trace.Assert(Math.Abs(b*l2[i]-b_times_v2[i])<delta);
                }
                Console.WriteLine($"* passed, n={n}");
            }
            Console.WriteLine("89weyf98weyfy");
	        return 0;
        }
    }
}
"""

        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=5)
        print(ret)
        
        for n in range(1, 10):
            self.assertTrue(f'return type passed, n={n}' in ret, f'Multiplication returned wrong type, n={n}')
            self.assertTrue(f'* passed, n={n}' in ret, f'Multiplication failed with, n={n}')

        self.assertTrue('89weyf98weyfy' in ret, 'Test failed, unknown error!')
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

