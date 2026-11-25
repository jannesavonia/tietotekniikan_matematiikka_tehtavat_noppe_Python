using System;
/*
M21

Kirjoita funktiot T(dx) ja S(c), jotka palauttavat matriisit, jotka
vastaavat siirrosta dx:n verran ja skaalausta vakiolla c
*/
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;

namespace Lineaarialgebra
{
    class MyProgram {
		public static Matrix<double> T(double dx) {
			//Your code here!
		}
    
		public static Matrix<double> S(double c) {
			//Your code here!
		}

		
	    #if !TEST_FLAG_DO_NOT_REMOVE    
		static void Main() {
    		double epsilon=0.0001;
			Random rnd=new Random();

			for(int i=0; i<100; i++) {
				Vector<double> x=CreateVector.Dense(new double[] {rnd.NextDouble(), 1});
				double x_real=x[0];
				for(int j=0; j<10; j++) {
					double c=1+5*rnd.NextDouble();
					double dx=1+2*rnd.NextDouble();
					x=T(dx)*x;
					x=S(c)*x;
					x_real+=dx;
					x_real*=c;
				}
				Trace.Assert(Math.Abs(x_real-x[0])<epsilon);
			}
		}
		#endif
    }
}
