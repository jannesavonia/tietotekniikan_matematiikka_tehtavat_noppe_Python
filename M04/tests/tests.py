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
    def test_Python(self):
        #Test python program
        self.startTest()
        res=callmain(cmdline_args=[], input='')

        #remove non alpha characters
        msg=''
        for c in res:
            if c.isalpha():
                msg=msg+c.upper()
        self.assertEqual(len(msg), 1822, 'Length of decoded message not correct!')

        hash=0
        for idx, c in enumerate(msg):
            hash+=(idx*idx+11)*ord(c)

        self.assertEqual(hash, 152597428157, 'Decrypted message not correct')
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

