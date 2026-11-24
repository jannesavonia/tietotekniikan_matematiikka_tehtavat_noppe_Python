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

from my_code import keys

print('test begin')

testdata={
  (23, 11, 3): ((253, 3), (253, 147)),
  (12601, 6043, 17): ((76147843, 17), (76147843, 17912753)),
  (1367, 20743, 257): ((28355681, 257), (28355681, 11575973))
}

for par, res in testdata.items():
    print(f'test keys{par}...', end='')
    Kpub, Kpriv=keys(*par)
    if Kpub!=res[0]:
        print(f'returned Kpub={Kpub} != {res[0]}, test failed')
        exit()
    if Kpriv!=res[1]:
        print(f'returned Kpriv={Kpriv} != {res[1]}, test failed')
        exit()
    print('ok')

print('test exception if syt(e, phi(p, q))!=1...', end='')
try:
    Kpub, Kpriv=keys(13, 101, 5)
    print('keys(13, 101, 5) did not generate an exception - test failed')
    exit()
except:
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
                23, 11, 3,
                  253, 147,
                12601, 6043, 17,
                  76147843, 17912753,
                1367, 20743, 257,
                  28355681, 11575973
	        };

            int N=testdata.Length;
            for(int i=0; i<N; i+=5) {
                ulong p, q, e, n, d, n_exp, d_exp;
                p=testdata[i];
                q=testdata[i+1];
                e=testdata[i+2];
                n_exp=testdata[i+3];
                d_exp=testdata[i+4];
                n=0;
                d=0;
                Console.Write($"test keys({p}, {q}, {e}, ...)");
                MyProgram.keys(p, q, e, ref n, ref d);

                var Kpub=(n, e);
			    var Kpriv=(n, d);

                if(Kpub!=(n_exp, e)) {
                    Console.WriteLine($"returned Kpub={Kpub} != {(n_exp, e)}, test failed");
                    return -1;
                } 
                if(Kpriv!=(n_exp, d_exp)) {
                    Console.WriteLine($"returned Kpriv={Kpriv} != {(n_exp, d_exp)}, test failed");
                    return -1;
                } 
                
                Console.WriteLine("ok");
	        }

            Console.Write("test exception if syt(e, phi(p, q))!=1...");
            try {
                ulong p, q, e, n, d;
                p=13;
                q=101;
                e=5;
                n=0;
                d=0;
                MyProgram.keys(p, q, e, ref n, ref d);
                Console.WriteLine("keys(13, 101, 5, ...) did not generate an exception - test failed");
                return -1;
            } catch {
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

