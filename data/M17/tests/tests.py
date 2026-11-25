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

v1=Vect([17, 0.1, -11])
v2=Vect([-12, 11, 0.2])

delta=0.01
assert abs(v1@v2-(-205.1))<delta
assert abs(v2@v1-(-205.1))<delta
print('first test passed')


for n in range(1, 10):
    l1=[rnd.uniform(-10, 10) for i in range(n)]
    l2=[rnd.uniform(-10, 10) for i in range(n)]
    l3=[rnd.uniform(-10, 10) for i in range(n)]
    
    v1=Vect(l1)
    v2=Vect(l2)
    v3=Vect(l3)

    norm_v1=v1.norm()
    norm_v2=v2.norm()
    norm_v3=v3.norm()

    delta=0.01
    assert abs(v1@v1-(norm_v1**2))<delta
    assert abs(v2@v2-(norm_v2**2))<delta
    assert abs(v3@v3-(norm_v3**2))<delta
    assert abs(v1@v2)<=norm_v1*norm_v2+delta
    assert abs(v2@v3)<=norm_v2*norm_v3+delta
    assert abs(v3@v1)<=norm_v3*norm_v1+delta
    print(f'norm passed, n={n}')

    v0=Vect([0 for _ in range(11)])
    try:
        z=v0@v1
    except:
        print(f'exception passed, n={n}')

print('uisdhdfy87sdyf87')
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
            double delta=0.01;

            double[] ll=new double[] {17, 0.1, -11};
            double[] kk=new double[] {-12, 11, 0.2};
            Vect vv1=new Vect(ll);
            Vect vv2=new Vect(kk);

            Trace.Assert(Math.Abs(vv1*vv2-(-205.1))<delta);
            Trace.Assert(Math.Abs(vv1*vv2-(-205.1))<delta);
            Console.WriteLine("first test passed");


            for(int n=1; n<10; n++) {
                var l1=new double[n];
                var l2=new double[n];
                var l3=new double[n];
 
                for(int i=0; i<n; i++) {
                    l1[i]=20.0*(rnd.NextDouble()-0.5);
                    l2[i]=20.0*(rnd.NextDouble()-0.5);
                    l3[i]=20.0*(rnd.NextDouble()-0.5);
                }

                var v1=new Vect(l1);
                var v2=new Vect(l2);
                var v3=new Vect(l3);

                double norm_v1=v1.norm();
                double norm_v2=v2.norm();
                double norm_v3=v3.norm();

                Trace.Assert(Math.Abs(v1*v1-(norm_v1*norm_v1))<delta);
                Trace.Assert(Math.Abs(v2*v2-(norm_v2*norm_v2))<delta);
                Trace.Assert(Math.Abs(v3*v3-(norm_v3*norm_v3))<delta);
                Trace.Assert(Math.Abs(v1*v2)<=norm_v1*norm_v2+delta);
                Trace.Assert(Math.Abs(v2*v3)<=norm_v2*norm_v3+delta);
                Trace.Assert(Math.Abs(v3*v1)<=norm_v3*norm_v1+delta);
                Console.WriteLine($"norm passed, n={n}");

                double[] l0=new double[11];
                Vect v0=new Vect(l0);
                try {
                    double z=v0*v1;
                } catch {
                    Console.WriteLine($"exception passed, n={n}");
                }

           }
            Console.WriteLine("uisdhdfy87sdyf87");
	        return 0;
        }
    }
}

"""

        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=5)
        print(ret)
        
        self.assertTrue('first test passed' in ret, 'Dot product test failed')
        for n in range(1, 10):
            self.assertTrue(f'norm passed, n={n}' in ret, f'norm(v)^2 !=  v@v with n={n}')
            self.assertTrue(f'exception passed, n={n}' in ret, f'no exception with dimension error with n={n}')

        self.assertTrue('uisdhdfy87sdyf87' in ret, 'Test failed, unknown error!')
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

