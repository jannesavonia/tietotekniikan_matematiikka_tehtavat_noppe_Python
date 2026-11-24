import sys
import unittest
import os
import re

new_wd=os.path.dirname(os.path.abspath(__file__))
os.chdir(new_wd)

def split(s):
    return re.split('/|\\\\', s)

"""
#Find path to current root
pathlist=split(sys.argv[0])
if len(pathlist)==1:
    path='./'
else:
    path=pathlist[0]+'/'
"""

path=new_wd+'/'
testpath=path+'tests/'

resultfile=testpath+'/result.txt'
try:
    os.remove(resultfile)
except:
    pass

sys.path.insert(0, testpath)
sys.path.insert(0, path+'src')
sys.path.insert(0, path+'../helpers')

print('Test', testpath, new_wd)


#Import code to test
from tests import *

curr_file=os.path.abspath(__file__)
exname = split(curr_file)[-2]

print('Test', exname, testpath)

#if __name__ == '__main__':
unittest.main(verbosity=4, exit=False)

outputfile=open(resultfile, 'wt')
outputfile.write('{0}\t{1}'.format(completed(), started()))
outputfile.close()
if started()>completed():
    print(started()-completed(), '/', started(), 'tests failed!')
else:
    print(completed(),'tests completed succesfully')

