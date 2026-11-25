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

a_2_6=Mod(2, 6)
a_7_6=Mod(7, 6)
b_1_5=Mod(1, 5)

print('  test exception if a.n!=b.n...', end='')
try:
    c=a_2_6+b_1_5
    print('test failed')
    exit()
except:
    print('ok')

print('  test ==...', end='')
if Mod(7, 5)==Mod(2, 5) and not Mod(7, 5)==Mod(3, 5):
    print('ok')
else:
    print('test failed')
    exit()

print('  test +...', end='')
c=a_2_6+a_7_6
if c==Mod(3, 6):
    print('ok')
else:
    print(f'test failed: got {a_2_6}+{a_7_6} = {a_2_6+a_7_6}')
    exit()

print('  test -...', end='')
c=a_2_6-a_7_6
if c==Mod(1, 6):
    print('ok')
else:
    print(f'test failed: got {a_2_6}-{a_7_6} = {a_2_6-a_7_6}')
    exit()


print('  test *...', end='')
a_9_6=Mod(9, 6)
c=a_2_6*a_9_6
if c==Mod(0, 6):
    print('ok')
else:
    print(f'test failed: got {a_2_6}-{a_9_6} = {a_2_6*a_9_6}')
    exit()

print('  test **...', end='')
c_8_3=Mod(8, 3)
c=c_8_3**1755
if c==Mod(2, 3):
    print('ok')
else:
    print(f'test failed: got {c_8_3}**17 = {c}')
    exit()

print('  test ** with negative exponent...', end='')
try:
    d=c**(-1)
    print('test failed')
    exit()
except:
    print('ok')

print('  test ** with non-integer exponent...', end='')
try:
    d=c**1.5
    print('test failed')
    exit()
except:
    print('ok')

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

            Mod a_2_6=new Mod(2, 6);
            Mod a_7_6=new Mod(7, 6);
            Mod b_1_5=new Mod(1, 5);

            Console.Write("  test exception if a.n!=b.n...");
            try {
                Mod c=a_2_6+b_1_5;
                Console.WriteLine("test failed");
                return -1;
            } catch {
                Console.WriteLine("ok");
            }

            Console.Write("  test ==...");
            Mod a_7_5=new Mod(7, 5);
            Mod b_2_5=new Mod(2, 5);
            Mod c_3_5=new Mod(3, 5);
            if(a_7_5==b_2_5 &&  a_7_5!=c_3_5) {
                Console.WriteLine("ok");
            } else {
                Console.WriteLine("test failed");
                return -1;
            }

            Console.Write("  test +...");
            Mod c1=a_2_6+a_7_6;
            if(c1==new Mod(3, 6)) {
                Console.WriteLine("ok");
            } else {
                Console.WriteLine($"test failed: got {a_2_6}+{a_7_6} = {c1}");
                return -1;
            }

            Console.Write("  test -...");
            Mod c2=a_2_6-a_7_6;
            if(c2==new Mod(1, 6)) {
                Console.WriteLine("ok");
            } else {
                Console.WriteLine($"test failed: got {a_2_6}-{a_7_6} = {c2}");
            }

            Console.Write("  test *...");
            Mod a_9_6=new Mod(9, 6);
            Mod c3=a_2_6*a_9_6;
            Mod c_0_6=new Mod(0, 6);
            if(c3==c_0_6) {
                Console.WriteLine("ok");
            } else {
                Console.WriteLine($"test failed: got {a_2_6}-{a_9_6} = {c3}");
            }

            Console.Write("  test pow()...");
            Mod c_8_3=new Mod(8, 3);
            Mod c4=c_8_3.pow(1755);
            Mod c_2_3=new Mod(2, 3);
            if(c4==c_2_3) {
                Console.WriteLine("ok");
            } else {
                Console.WriteLine($"test failed: got {c_8_3}**17 = {c4}");
                return -1;
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
                         'test completed': 'Test terminated'}

        for tt, eo in expected_output.items():
            print('  Test "'+tt+'":')
            self.assertTrue(eo in ret)


        not_expected_output={'test failed'    : 'test failed'}

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

