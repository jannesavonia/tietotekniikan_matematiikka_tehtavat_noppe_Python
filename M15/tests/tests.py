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

    len1=sum([x*x for x in l1])
    a_len1=abs(a*a)*len1
    len2=sum([x*x for x in l2])
    b_len2=abs(b*b)*len2

    delta=0.01
    assert abs(len1-(v1.norm()**2))<delta
    assert abs(a_len1-((a*v1).norm()**2))<delta
    assert abs(len2-(v2.norm()**2))<delta
    assert abs(b_len2-((b*v2).norm()**2))<delta
    print(f'norm passed, n={n}')

    v3=v1+v2

    len2=sum([x*x for x in l2])

    delta=0.01
    assert abs(len2-(Vect.dist(v1, v3)**2))<delta
    print(f'dist passed, n={n}')


print('2io3u4234u89u34')
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
                var a=20.0*(rnd.NextDouble()-0.5);
                var b=20.0*(rnd.NextDouble()-0.5);

                double len1=0.0;
                double a_len1=0.0;
                double len2=0.0;
                double b_len2=0.0;

                for(int i=0; i<n; i++) {
                    l1[i]=20.0*(rnd.NextDouble()-0.5);
                    l2[i]=20.0*(rnd.NextDouble()-0.5);
                    len1+=l1[i]*l1[i];
                    len2+=l2[i]*l2[i];
                    a_len1+=a*a*l1[i]*l1[i];
                    b_len2+=b*b*l2[i]*l2[i];
                }

                var v1=new Vect(l1);
                var v2=new Vect(l2);

                Trace.Assert(Math.Abs(len1-(v1.norm()*v1.norm()))<delta);
                Trace.Assert(Math.Abs(a_len1-((a*v1).norm()*(a*v1).norm()))<delta);
                Trace.Assert(Math.Abs(len2-(v2.norm()*v2.norm()))<delta);
                Trace.Assert(Math.Abs(b_len2-((b*v2).norm()*(b*v2).norm()))<delta);
                Console.WriteLine($"norm passed, n={n}");

                Vect v3=v1+v2;
                len2=v2.norm()*v2.norm();

                Trace.Assert(Math.Abs(len2-(Vect.dist(v1, v3)*Vect.dist(v1, v3)))<delta);
                Console.WriteLine($"dist passed, n={n}");
           }
            Console.WriteLine("2io3u4234u89u34");
	        return 0;
        }
    }
}
"""

        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=5)
        #print(ret)
        
        for n in range(1, 10):
            self.assertTrue(f'norm passed, n={n}' in ret, f'norm failed with n={n}')
            self.assertTrue(f'dist passed, n={n}' in ret, f'dist failed with n={n}')

        self.assertTrue('2io3u4234u89u34' in ret, 'Test failed, unknown error!')
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

