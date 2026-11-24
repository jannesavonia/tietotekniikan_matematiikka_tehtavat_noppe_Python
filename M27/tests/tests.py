import unittest
from helpers import *
#import timeout_decorator

#Never do following! The test process can be halted by student code!
#from my_code import *

def rmoutput():
    for filename in ['src/output.txt']:
        try:
            os.remove(filename)
            print(f'Removed {filename}')
        except:
            pass


started_tests = 0
completed_tests = 0

class TestCode(unittest.TestCase):
    def test_PythonFunction(self):
        #Test python function (in this case function name is combine)
        #Test code (my_code) must be implemented
        rmoutput()
        self.startTest()

        py_code="""
import sys
import random as rnd
sys.path.insert(0, '../src')

import numpy as np
from my_code import euler_spiral, filename
import pandas as pd

def compare_xy(data, t, x, y):
    d=data.loc[(t-eps<data['t']) & (data['t']<t+eps)]
    dx=float(d['x'].iloc[0])
    dy=float(d['y'].iloc[0])
    
    #print(dx, dy)

    return abs(dx-x), abs(dy-y)

N=100
dt=0.04
euler_spiral(dt, N)
data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])

precomputed_values=np.array([[0.36, 0.9304886467391792, 0.3367306350942747],
                                [2.68, -0.6029065037979954, -0.1867161903878204],
                                [4.0, 0.2035872095370079, -0.4510259183348253]])

                                
if len(data)!=N+1:
    print('ERROR: length of data')

if len(data.columns)!=3:
    print('ERROR: number of columns')

eps=0.001

if abs(data['t'].min()-0)>eps:
    print('ERROR: min(t)!=0')

if abs(data['t'].max()-N*dt)>eps:
    print('ERROR: max(t)!=n*Dt')


for t, x, y in precomputed_values:
    dx,dy=compare_xy(data, t, x, y)
    if dx>eps:
        print('ERROR: Wrong x-value!')
    if dy>eps:
        print('ERROR: Wrong y-value!')

        
N=10000
dt=0.0011
euler_spiral(dt, N)
data=pd.read_csv(filename, delimiter=' ', names=['t','x','y'])

precomputed_values=np.array([[0.3608, 0.9225249318121936, 0.3328443083004586],
                                [2.684, -0.5310574085412356, -0.2145523016162695],
                                [4.026, 0.25136075967316, -0.2943525796821433]])

if len(data)!=N+1:
    print('ERROR: length of data')

if len(data.columns)!=3:
    print('ERROR: number of columns')

eps=0.0001

if abs(data['t'].min()-0)>eps:
    print('ERROR: min(t)!=0')

if abs(data['t'].max()-N*dt)>eps:
    print('ERROR: max(t)!=n*Dt')

for t, x, y in precomputed_values:
    dx,dy=compare_xy(data, t, x, y)
    if dx>eps:
        print('ERROR: Wrong x-value!')
    if dy>eps:
        print('ERROR: Wrong y-value!')

print('827498732498723')
"""
        cs_code="""
using System;
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;
using System.IO;
using MathNet.Numerics.Data.Text;

namespace Lineaarialgebra
{
    class TestProgram {

		static int t_col_idx=0;
		static int x_col_idx=1;
		static int y_col_idx=2;

		static void compare_xy(Matrix<double> data, double t, double x, double y, ref double dx, ref double dy, double dt) {
			dx=1000000000.0;
			dy=1000000000.0;
			for(int i=0; i<data.RowCount; i++) {
				Vector<double> row=data.Row(i);
				double t_data=row[t_col_idx];
				if(t_data>t-dt/2 && t_data<t+dt/2) {
					dx=Math.Abs(x-row[x_col_idx]);
					dy=Math.Abs(y-row[y_col_idx]);
					return;
				}
			}
		}
		static void Main() {
			string filename="output.txt";

            int N=100;
            double dt=0.04;
    		MyProgram.euler_spiral(dt, N, filename);

			Matrix<double> data = DelimitedReader.Read<double>(filename, false, " ", false);

            double[,] precomputed_values=new double[,] {{0.36, 0.9304886467391792, 0.3367306350942747},
                                {2.68, -0.6029065037979954, -0.1867161903878204},
                                {4.0, 0.2035872095370079, -0.4510259183348253}};
        
			if(data.RowCount!=N+1) {
                Console.WriteLine("ERROR: length of data");
            }
			if(data.ColumnCount!=3) {
                Console.WriteLine("ERROR: number of columns");
            }

			Vector<double> t_col=data.Column(t_col_idx);
			Vector<double> x_col=data.Column(x_col_idx);
			Vector<double> y_col=data.Column(y_col_idx);

			double eps=0.001;
    		if(Math.Abs(t_col.Minimum()-0)>eps) {
                Console.WriteLine("ERROR: min(t)!=0");
            }
    		if(Math.Abs(t_col.Maximum()-N*dt)>eps) {
                Console.WriteLine("ERROR: max(t)!=n*Dt");
            }

			for(int i=0; i<precomputed_values.GetLength(0); i++) {
				double t=precomputed_values[i, t_col_idx];
				double x=precomputed_values[i, x_col_idx];
				double y=precomputed_values[i, y_col_idx];
				double dx=0;
				double dy=0;

				compare_xy(data, t, x, y, ref dx, ref dy, dt);

				if(dx>eps) {
                    Console.WriteLine("ERROR: Wrong x-value!");
                }
				if(dy>eps) {
                    Console.WriteLine("ERROR: Wrong y-value!");
                }
			}

			N=10000;
    		dt=0.0011;

            precomputed_values=new double[,] {{0.3608, 0.9225249318121936, 0.3328443083004586},
                                {2.684, -0.5310574085412356, -0.2145523016162695},
                                {4.026, 0.25136075967316, -0.2943525796821433}};

    		MyProgram.euler_spiral(dt, N, filename);
			data = DelimitedReader.Read<double>(filename, false, " ", false);
			for(int i=0; i<precomputed_values.GetLength(0); i++) {
				double t=precomputed_values[i, t_col_idx];
				double x=precomputed_values[i, x_col_idx];
				double y=precomputed_values[i, y_col_idx];
				double dx=0;
				double dy=0;

				compare_xy(data, t, x, y, ref dx, ref dy, dt);

				if(dx>eps) {
                    Console.WriteLine("ERROR: Wrong x-value!");
                }
				if(dy>eps) {
                    Console.WriteLine("ERROR: Wrong y-value!");
                }

			}

            Console.WriteLine("827498732498723");
		}
    }
}
"""
        ret=callcode(pycode=py_code, cscode=cs_code, input='', timeout=5)
        #print(ret)
        
        self.assertTrue('ERROR: length of data' not in ret, 'ERROR: length of data')
        self.assertTrue('ERROR: number of columns' not in ret, 'ERROR: number of columns')
        self.assertTrue('ERROR: min(t)!=0' not in ret, 'ERROR: min(t)!=0')
        self.assertTrue('ERROR: max(t)!=n*Dt' not in ret, 'ERROR: max(t)!=n*Dt')
        self.assertTrue('ERROR: Wrong x-value!' not in ret, 'ERROR: Wrong x-value!')
        self.assertTrue('ERROR: Wrong y-value!' not in ret, 'ERROR: Wrong y-value!')

        self.assertTrue('827498732498723' in ret, 'Test failed, unknown error!')
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

