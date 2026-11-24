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


print('Test begin')
K={
        'A': 'K',
        'B': 'B',
        'C': 'N',
        'D': 'L',
        'E': 'M',
        'F': 'A',
        'G': 'O',
        'H': 'F',
        'I': 'G',
        'J': 'H',
        'K': 'W',
        'L': 'X',
        'M': 'Y',
        'N': 'Z',
        'O': 'P',
        'P': 'Q',
        'Q': 'T',
        'R': 'U',
        'S': 'R',
        'T': 'S',
        'U': 'E',
        'V': 'V',
        'W': 'C',
        'X': 'I',
        'Y': 'D',
        'Z': 'J'
}

M="this is a test message."
C=E(K,M)
print('#'+C+'#')

if C!='SFGR GR K SMRS YMRRKOM.':
    print('Invalid encrypted message!')

Mrec=D(K,C)
print('*'+Mrec+'*')
if M.upper()!=Mrec:
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
            
            var K= new Dictionary<char, char>() {
                {'A', 'K'},
                {'B', 'B'},
                {'C', 'N'},
                {'D', 'L'},
                {'E', 'M'},
                {'F', 'A'},
                {'G', 'O'},
                {'H', 'F'},
                {'I', 'G'},
                {'J', 'H'},
                {'K', 'W'},
                {'L', 'X'},
                {'M', 'Y'},
                {'N', 'Z'},
                {'O', 'P'},
                {'P', 'Q'},
                {'Q', 'T'},
                {'R', 'U'},
                {'S', 'R'},
                {'T', 'S'},
                {'U', 'E'},
                {'V', 'V'},
                {'W', 'C'},
                {'X', 'I'},
                {'Y', 'D'},
                {'Z', 'J'}
            };
            
            string C=MyProgram.E(ref K,M);
            Console.WriteLine("#"+C+"#");
            if(C!="SFGR GR K SMRS YMRRKOM.") {
                Console.WriteLine("Invalid encrypted message!");
            }

            string Mrec=MyProgram.D(ref K,C);
            Console.WriteLine("*"+Mrec+"*");
            if(M.ToUpper()!=Mrec) {
                Console.WriteLine("Messages does not match!");
            }

            Console.WriteLine("Test terminated");
	        return 0;
        }
    }
}
"""

        ret=callcode(pycode=py_code, cscode=cs_code, input='')

        print(ret)

        expected_output={'test begin'    : 'Test begin',
                         'encoded text'  : '#SFGR GR K SMRS YMRRKOM.#',
                         'decrypted text': '*THIS IS A TEST MESSAGE.*',
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

