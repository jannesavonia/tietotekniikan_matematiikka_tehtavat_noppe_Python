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
        C='MUUN JCMNYYH NUMNU NYBNUPUMNU'
        
        #Test python or C# program
        self.startTest()
        res=callmain(cmdline_args=[], input='')
        M_candidates=res.split('\n')
        count={}
        decrypted_found=False
        for M in M_candidates:
            M=M.strip()
            if M=='':
                continue
            print(f'Check "{M}"')
            self.assertEqual(len(C), len(M), 'Lenght of decrypted message is not same as length of encrypted message!')
            s=0
            for idx, c in enumerate(M):
                if c.isalpha():
                    if c not in count:
                        count[c]=1
                    else:
                        count[c]+=1
                s+=(idx+1)*ord(c)
            if s==31324:
                decrypted_found=True
            

        self.assertEqual(len(C.replace(' ', '')), min(count.values()), 'Wrong amount of decrypted messages or failed decrypting process')
        self.assertTrue(decrypted_found, 'No correct decrypted message found on output!')
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

