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

    u1=v1.unit()
    u2=v2.unit()

    delta=0.01
    norm_u1=u1.norm()
    norm_u2=u2.norm()

    delta=0.01
    assert abs(1-norm_u1)<delta
    assert abs(1-norm_u2)<delta
    print(f'length passed, n={n}')

    uu1=v1.norm()*u1
    assert((v1-uu1).norm()<delta)
    uu2=v2.norm()*u2
    assert((v2-uu2).norm()<delta)
    print(f'direction passed, n={n}')

    v0=Vect([0 for _ in range(n)])
    try:
        u0=v0.unit()
    except:
        print(f'exception passed, n={n}')

print('y87yf87afy78syf')
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
            for(int n=1; n<10; n++) {
                var l1=new double[n];
                var l2=new double[n];
 
                for(int i=0; i<n; i++) {
                    l1[i]=20.0*(rnd.NextDouble()-0.5);
                    l2[i]=20.0*(rnd.NextDouble()-0.5);
                }

                var v1=new Vect(l1);
                var v2=new Vect(l2);
                Vect u1=v1.unit();
                Vect u2=v2.unit();

                double norm_u1=u1.norm();
                double norm_u2=u2.norm();
                Console.WriteLine($"length passed, n={n}");

                Vect uu1=v1.norm()*u1;
                Trace.Assert((v1-uu1).norm()<delta);
                Vect uu2=v2.norm()*u2;
                Trace.Assert((v2-uu2).norm()<delta);
                Console.WriteLine($"direction passed, n={n}");

                double[] l0=new double[n];
                for(int i=0; i<n; i++) {
                    l0[i]=0;
                }
                Vect v0=new Vect(l0);
                try {
                    Vect u0=v0.unit();

                } catch {
                    Console.WriteLine($"exception passed, n={n}");
                }
           }
            Console.WriteLine("y87yf87afy78syf");
	        return 0;
        }
    }
}
"""
        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=5)
        #print(ret)
        
        for n in range(1, 10):
            self.assertTrue(f'length passed, n={n}' in ret, f'norm failed with n={n}')
            self.assertTrue(f'direction passed, n={n}' in ret, f'dist failed with n={n}')
            self.assertTrue(f'exception passed, n={n}' in ret, f'0-vector exception failed with n={n}')

        self.assertTrue('y87yf87afy78syf' in ret, 'Test failed, unknown error!')
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

