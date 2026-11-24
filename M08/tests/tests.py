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

from my_code import phi

print('test begin')

testdata={
  1   :   1,
  2   :   1,
  3   :   2,
  10  :   4,
  17  :  16,
  242 : 110,
  251 : 250,
  500 : 200,
  434 : 180,
}

for n, phi_n in testdata.items():
    print(f'phi({n}) ?= {phi_n}...', end='')
    p=phi(n)
    if p==phi_n:
        print('ok')
    else:
        print(f'phi({n}) returned {p} - test failed')
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
                1   ,   1,
                2   ,   1,
                3   ,   2,
                10  ,   4,
                17  ,  16,
                242 , 110,
                251 , 250,
                500 , 200,
                434 , 180
            };

            for(int i=0; i<testdata.Length; i+=2) {
                ulong n=testdata[i];
                ulong phi_n=testdata[i+1];
                ulong p=MyProgram.phi(n);
                Console.Write($"phi({n}) ?= {phi_n}...");
                if(p==phi_n) {
                    Console.WriteLine("ok");
                } else {
                    Console.WriteLine($"phi({n}) returned {p} - test failed");
                    return -1;
                }
            }

            Console.WriteLine("test complete");
	        return 0;
        }
    }
}
"""

        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=60)
        
        print(ret)

        self.assertTrue('test failed' not in ret, 'test failed')
            
        expected_output={'test begin'         :'test not started',
                         'test complete'      :'test crashed'}

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

