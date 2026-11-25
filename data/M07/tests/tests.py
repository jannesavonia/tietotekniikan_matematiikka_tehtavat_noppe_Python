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

from my_code import sieve

print('test begin')

P=sieve(999982)
if len(P)==78497:
    print('number of primes ok')
else:
    print('number of primes not ok - test failed')
    exit()

numbers=[2, 3, 5, 7, 11, 101, 
         999931,999953,999959,999961,999979,
         291173,291191,291199,291209,291217,291253,291257,
         99907, 99923, 99929, 99961, 99971, 99989, 99991,
         78487, 78497, 78509, 78511, 78517,
         17623,	17627, 17657, 17659, 17669
         ]

print('test primes...', end='')
for n in numbers:
    if n not in P:
        print(f'{n} not found in primes set - test failed')
        exit()
print('ok')

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

            var P=MyProgram.sieve(999982);
            if(P.Count==78497) {
                Console.WriteLine("number of primes ok");
            } else {
                Console.WriteLine("number of primes not ok - test failed");
                return -1;
            }

            ulong[] numbers=new ulong[] {
                2, 3, 5, 7, 11, 101, 
                999931,999953,999959,999961,999979,
                291173,291191,291199,291209,291217,291253,291257,
                99907, 99923, 99929, 99961, 99971, 99989, 99991,
                78487, 78497, 78509, 78511, 78517,
                17623,	17627, 17657, 17659, 17669
            };

            Console.Write("test primes...");
            foreach(var n in numbers) {
                if(!P.Contains(n)) {
                    Console.WriteLine($"{n} not found in primes set - test failed");
                    return -1;
                }
            }
            Console.WriteLine("ok");

            Console.WriteLine("test complete");
	        return 0;
        }
    }
}
"""
        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=600)
        
        print(ret)

        self.assertTrue('test failed' not in ret, 'sieve(999982) returned wrong set')
            
        expected_output={'test begin'         :'test not started',
                         'number of primes ok':'number of primes not ok',
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

