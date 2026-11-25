import unittest
from helpers import *
#import timeout_decorator

#Never do following! The test process can be halted by student code!
#from my_code import *

def rmoutput():
    for filename in []:
        try:
            os.remove(filename)
        except:
            pass


started_tests = 0
completed_tests = 0

class TestCode(unittest.TestCase):
    def test_PythonFunction(self):
        #Test python function (in this case function name is combine)
        #Test code (my_code) must be implemented
        self.startTest()

        py_code="""
import sys
import random as rnd
sys.path.insert(0, '../src')

import numpy as np
from my_code import rotate_around_point

epsilon=0.0001

for i in range(100):
    point=np.random.randn(2)
    point=np.append(point, [1])
    N=i
    X=np.random.randn(3, N)
    X[-1, :]=1 #Set 3rd coordinate as 1
    
    a=rnd.gauss(0, 16*np.pi)
    Z=rotate_around_point(a, point, X)

    for i in range(N):
        x=X[:, i]
        z=Z[:, i]
        #Check center of rotation
        if abs(np.linalg.norm(point-x)-np.linalg.norm(point-z))>epsilon:
            print('ERROR: Center of rotation is wrong')

        #Check rotation angle
        b=np.arccos(((x-point)@(z-point))/(np.linalg.norm(z-point)**2))
        if abs(np.cos(b)-np.cos(a))>epsilon:
            print('ERROR: Rotation angle wrong')

print('988say89yd')
"""
        cs_code="""
using System;
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;

namespace Lineaarialgebra
{
    class TestProgram {
		static void Main() {
    		double epsilon=0.0001;
			Random rnd=new Random();

			for(int i=0; i<100; i++) {
				Vector<double> point=CreateVector.Dense(new double[]{10*rnd.NextDouble(), 10*rnd.NextDouble(), 1});
				int N=i;

				double[,] lx=new double[3, N];
				for(int j=0; j<N; j++) {
					for(int k=0; k<2; k++) {
						lx[k, j]=10*rnd.NextDouble();
					}
					lx[2, j]=1;
				}
				Matrix<double> X=CreateMatrix.DenseOfArray(lx);

				double a=16*3.14159265*rnd.NextDouble();

				Matrix<double> Z=MyProgram.rotate_around_point(a, point, X);
				for(int j=0; j<N; j++) {
					Vector<double> x=X.Column(j);
					Vector<double> z=Z.Column(j);
					//Check center of rotation
                    if(Math.Abs((point-x).L2Norm()-(point-z).L2Norm())>epsilon) {
                        Console.WriteLine("ERROR: Center of rotation is wrong");
                    }
					//Check rotation angle
					double b=Math.Acos((x-point)*(z-point)/((z-point).L2Norm()*(z-point).L2Norm()));
					if(Math.Abs(Math.Cos(b)-Math.Cos(a))>epsilon) {
                        Console.WriteLine("ERROR: Rotation angle wrong");
                    }
				}
			}
            Console.WriteLine("988say89yd");
		}
    }
}
"""

        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=5)
        #print(ret)
        
        self.assertTrue('ERROR: Center of rotation is wrong' not in ret, 'ERROR: Center of rotation is wrong')
        self.assertTrue('ERROR: Rotation angle wrong' not in ret, 'ERROR: Rotation angle wrong')

        self.assertTrue('988say89yd' in ret, 'Test failed, unknown error!')
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

