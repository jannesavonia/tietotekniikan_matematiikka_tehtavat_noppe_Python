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

from my_code import *

K=(2,9,5,4,8,6,3,7,1)
print('Test begin')

M="this is a test message."
C=E(K,M)
print('#'+C+'#')

if C!='atssii  hs mse ett s eg  .a':
    print('Invalid encrypted message!')

Mrec=D(K,C)
lM=len(M)
print('*'+Mrec[:lM]+'*')
if M!=Mrec[:lM]:
    print('Messages does not match!')

print('Test terminated')
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
            Console.WriteLine("Test begin");

            string M="this is a test message.";

            int[] K=new int[]{2,9,5,4,8,6,3,7,1};

            string C=MyProgram.E(ref K,M);
            Console.WriteLine("#"+C+"#");

            if(C!="atssii  hs mse ett s eg  .a") {
                Console.WriteLine("Invalid encrypted message!");
            }

            string Mrec=MyProgram.D(ref K,C);

            int lM=M.Length;
            Console.WriteLine("*"+Mrec.Substring(0, lM)+"*");

            if(M!=Mrec.Substring(0, lM)) {
                Console.WriteLine("Messages does not match!");
            }

            Console.WriteLine("Test terminated");

	        return 0;
        }
    }
}
"""
        ret=callcode(pycode=py_code, cscode=cs_code, input='')

        #print(ret)

        expected_output={'test begin'    : 'Test begin',
                         'encoded text'  : '#atssii  hs mse ett s eg  .a#',
                         'decrypted text': '*this is a test message.*',
                         'test completed': 'Test terminated'}

        for tt, eo in expected_output.items():
            print('  Test "'+tt+'":')
            self.assertTrue(eo in ret)


        not_expected_output={'encrypted message ok'    : 'Invalid encrypted message!',
                             'decrypted message ok'    : 'Messages does not match!'}

        for tt, neo in not_expected_output.items():
            print('  Test "'+tt+'":')
            self.assertTrue(neo not in ret)
            
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

