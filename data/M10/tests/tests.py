import unittest
from helpers import *

#Never do following! The test process can be halted by student code!
#from my_code import *



started_tests = 0
completed_tests = 0

def rmoutput():
    for filename in []:
        try:
            os.remove(filename)
        except:
            pass


class TestCode(unittest.TestCase):
    def test_PythonFunction(self):
        #Test python function (in this case function name is combine)
        #Test code (my_code) must be implemented
        self.startTest()

        py_code="""
import sys
sys.path.insert(0, '../src')

from my_code import syt_ext

print('test begin')

testdata={
  (100, 35): 5,
  (10, 35): 5,
  (3, 21): 3,
  (12378, 3054): 6,
  (48*17, 48*257): 48,
  (17*11*13*23, 257*23*17*5*7): 23*17,
  (257, 101): 1,
  (101, 257): 1
}

for ab, s in testdata.items(): 
  print(f'syt{ab} ?= {s}... ', end='')
  syt_ab, x, y=syt_ext(*ab)
  if s==syt_ab:
    print('ok')
  else:
    print(f'got syt{ab}={syt_ab}, test failed')
    exit()
  a, b=ab
  print(f'x={x}, y={y}', end=', ')
  print(f'{a}*{x}+{b}*{y} ?= {s}... ', end='')
  if s==a*x+b*y:
    print('ok')
  else:
    print(f'got {a}*{x}+{b}*{y} = {a*x+b*y}, test failed')
    exit()

print('test complete')
"""

        cs_code="""
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lukuteoria
{
    class MyTestProgram
    {
        static int Main(string[] args)
        {
            Console.WriteLine("test begin");

            ulong[] testdata=new ulong[] {
                100, 35, 5,
                10, 35, 5,
                3, 21, 3,
                12378, 3054, 6,
                48*17, 48*257, 48,
                17*11*13*23, 257*23*17*5*7, 23*17,
                257, 101, 1,
                101, 257, 1
	    };

            int N=testdata.Length;
            for(int i=0; i<N; i+=3) {
                ulong a=testdata[i];
                ulong b=testdata[i+1];
                ulong s=testdata[i+2];
                long x=0;
                long y=0;
                Console.Write($"syt({a}, {b}) ?= {s}... ");
                ulong syt_ab=MyProgram.syt_ext(a, b, ref x, ref y);
                if(s==syt_ab) {
                    Console.WriteLine("ok");
                } else {
                    Console.WriteLine($"got syt({a}, {b})={syt_ab}, test failed");
                    return -1;
                }
   
                Console.Write($"x={x}, y={y}, ");
                Console.Write($"{a}*{x}+{b}*{y} ?= {s}... ");
		long sum=(long)a*x+(long)b*y;
                if(((long)s)==sum) {
		    Console.WriteLine("ok");
                } else {
		    Console.WriteLine($"got {a}*{x}+{b}*{y} = {sum}, test failed");
		    return -1;
                }
	    }

            Console.WriteLine("test complete");
	    return 0;
        }
    }
}
"""

        ret=callcode(pycode=py_code, cscode=cs_code, input='')
        
        print(ret)

        self.assertTrue('test failed' not in ret, 'syt_ext(a, b) returned wrong value')
            
        expected_output={'test begin'    :'test not started',
                         'test complete' :'test crashed'}

        for eo, msg in expected_output.items():
            self.assertTrue(eo in ret, msg)

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

