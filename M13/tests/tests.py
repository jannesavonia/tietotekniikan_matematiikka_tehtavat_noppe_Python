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

    v1=Vect(l1)
    v2=Vect(l2)

    v1_plus_v2=v1+v2
    v1_minus_v2=v1-v2

    delta=0.01
    for i, _ in enumerate(l1):
        assert abs(v1[i]+v2[i]-v1_plus_v2[i])<delta
    print(f'+ passed, n={n}')

        
    for i, _ in enumerate(l1):
        assert abs(v1[i]-v2[i]-v1_minus_v2[i])<delta
    print(f'- passed, n={n}')

    for i, _ in enumerate(l1):
        assert abs(v1[i]-l1[i])<delta
        assert abs(v2[i]-l2[i])<delta
    print(f'[] passed, n={n}')

    #Test exception if adding mismatch vectors
    v3=Vect([1, 2, 3])
    try:
        v_error=v1+v3
    except:
        print(f'+ Exception passed, n={n}')

    #Test exception if subtracting mismatch vectors
    try:
        v_error=v1-v3
    except:
        print(f'- Exception passed, n={n}')

print('923u8293748937')
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

                for(int i=0; i<n; i++) {
                    l1[i]=20.0*(rnd.NextDouble()-0.5);
                    l2[i]=20.0*(rnd.NextDouble()-0.5);
                }

                var v1=new Vect(l1);
                var v2=new Vect(l2);

                var v1_plus_v2=v1+v2;
                var v1_minus_v2=v1-v2;

                double delta=0.01;

                for(int i=0; i<n; i++) {
                    Trace.Assert(Math.Abs(v1[i]+v2[i]-v1_plus_v2[i])<delta);
                }
                Console.WriteLine($"+ passed, n={n}");

                for(int i=0; i<n; i++) {
                    Trace.Assert(Math.Abs(v1[i]-v2[i]-v1_minus_v2[i])<delta);
                }
                Console.WriteLine($"- passed, n={n}");

                for(int i=0; i<n; i++) {
                    Trace.Assert(Math.Abs(v1[i]-l1[i])<delta);
                    Trace.Assert(Math.Abs(v2[i]-l2[i])<delta);
                }
                Console.WriteLine($"[] passed, n={n}");
            

                //Test exception if adding mismatch vectors
                double[] l3=new double[]{1, 2, 3};
                Vect v3=new Vect(l3);
                try{
                    Vect v_error=v1+v3;
                } catch {
                    Console.WriteLine($"+ Exception passed, n={n}");
                }
        
                //Test exception if subtracting mismatch vectors
                try{
                    Vect v_error=v1-v3;
                } catch {
                    Console.WriteLine($"- Exception passed, n={n}");
                }
            }
            Console.WriteLine("923u8293748937");
	        return 0;
        }
    }
}
"""

        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=5)
        print(ret)
        
        for n in range(1, 10):
            self.assertTrue(f'+ passed, n={n}' in ret, f'Add failed with n={n}')
            self.assertTrue(f'- passed, n={n}' in ret, f'Subtract failed with n={n}')
            self.assertTrue(f'[] passed, n={n}' in ret, f'[] failed with n={n}')
            if n!=3:
                self.assertTrue(f'+ Exception passed, n={n}' in ret, f'+ Exception failed with n={n}')
                self.assertTrue(f'- Exception passed, n={n}' in ret, f'- Exception with n={n}')

        self.assertTrue('923u8293748937' in ret, 'Test failed, unknown error!')
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

