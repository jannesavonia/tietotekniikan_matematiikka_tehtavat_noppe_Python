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

from my_code import E, D

print('test begin')

testdata={
  ((253, 3), (253, 147)): (55, 154),
  ((76147843, 17), (76147843, 17912753)): (2738, 27717276),
  ((28355681, 257), (28355681, 11575973)): (9283733, 18694630)
}

for par, res in testdata.items():
    Kpub, Kpriv=par
    M, C_expected=res

    print(f'test keys Kpub={Kpub}, Kpriv={Kpriv}, M={M}, C_expected={C_expected}...', end='')
    C=E(Kpub, M)
    #print(C) 
    if C!=C_expected:
        print(f'E({Kpub},{M}) returned {C}, while expected {C_expected} - test failed')
        exit()
    M_decoded=D(Kpriv, C)
    if M!=M_decoded:
        print(f'D({Kpriv},{C}) returned {M_decoded}, while expected {M} - test failed')
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

            ulong[] testdata=new ulong[] {
                //((253, 3), (253, 147)): (55, 154),
                //((76147843, 17), (76147843, 17912753)): (2738, 27717276),
                //((28355681, 257), (28355681, 11575973)): (9283733, 18694630)
                253, 3, 147,
                  55, 154,
                76147843, 17, 17912753,
                  2738, 27717276,
                28355681, 257, 11575973,
                  9283733, 18694630
	        };

            int N=testdata.Length;
            for(int i=0; i<N; i+=5) {
                var Kpub=(testdata[i], testdata[i+1]);
                var Kpriv=(testdata[i], testdata[i+2]);
                ulong M=testdata[i+3];
                ulong C_expected=testdata[i+4];
                Console.Write($"test keys Kpub={Kpub}, Kpriv={Kpriv}, M={M}, C_expected={C_expected}...");

                var C=MyProgram.E(Kpub.Item1, Kpub.Item2, M);
                if(C!=C_expected) {
                    Console.WriteLine($"E({Kpub.Item1}, {Kpub.Item2},{M}) returned {C}, while expected {C_expected} - test failed");
                    return -1;
                }

                var M_decoded=MyProgram.D(Kpriv.Item1, Kpriv.Item2, C);
                if(M!=M_decoded) {
                    Console.WriteLine($"D({Kpriv.Item1}, {Kpriv.Item2},{C}) returned {M_decoded}, while expected {M} - test failed");
                    return -1;
                }
                Console.WriteLine("ok");
	        }

            Console.WriteLine("test complete");
	        return 0;
        }
    }
}
"""
        ret=callcode(pycode=py_code, cscode=cs_code, input='')
        
        print(ret)

        self.assertTrue('test failed' not in ret, 'Test failed')
            
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

