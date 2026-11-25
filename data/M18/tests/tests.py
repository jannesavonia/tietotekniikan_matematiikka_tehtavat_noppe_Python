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

delta=0.01

for n in range(11, 20):
    l1=[rnd.uniform(-10, 10) for i in range(n)]
    l2=[rnd.uniform(-10, 10) for i in range(n)]
    l3=[rnd.uniform(-10, 10) for i in range(n)]
    
    v1=Vect(l1)
    v2=Vect(l2)
    v3=Vect(l3)

    p_v2_v1=v2.proj(v1)
    p_v2_v3=v2.proj(v3)
    p_v1_v3=v1.proj(v3)

    #Testataan, etta projektiot ovat oikein
    assert ((v1@v1)*p_v2_v1-(v1@v2)*v1).norm()<delta
    assert ((v3@v3)*p_v2_v3-(v3@v2)*v3).norm()<delta
    assert ((v3@v3)*p_v1_v3-(v3@v1)*v3).norm()<delta
    print(f'projection passed, n={n}')

print('7y87asyd87yasd8')
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

            for(int n=11; n<20; n++) {
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

			    Vect p_v2_v1=v2.proj(v1); //v2 projektio v1:lle
    		    Vect p_v2_v3=v2.proj(v3);
    		    Vect p_v1_v3=v1.proj(v3);

    		    Trace.Assert(((v1*v1)*p_v2_v1-(v1*v2)*v1).norm()<delta);
    		    Trace.Assert(((v3*v3)*p_v2_v3-(v3*v2)*v3).norm()<delta);
    		    Trace.Assert(((v3*v3)*p_v1_v3-(v3*v1)*v3).norm()<delta);
                Console.WriteLine($"projection passed, n={n}");
            }
            Console.WriteLine("7y87asyd87yasd8");
	        return 0;
        }
    }
}
"""

        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=5)
        #print(ret)
        
        for n in range(11, 20):
            self.assertTrue(f'projection passed, n={n}' in ret, f'projection failed with n={n}')

        self.assertTrue('7y87asyd87yasd8' in ret, 'Test failed, unknown error!')
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

