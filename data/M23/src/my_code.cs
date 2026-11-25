using System;
/*
M23
Kirjoita funktio direction(a, b), joka saa parametrina kaksi homogeenisen 
koordinaatiston paikkavektoria. Funktio palauttaa yksikkösuuntavektorin a:sta b:hen.
*/
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;

namespace Lineaarialgebra
{
    class MyProgram {
		static double epsilon=0.0001;

		public static Vector<double> direction(Vector<double> a, Vector<double> b) {
			//Your code here
		}
	    #if !TEST_FLAG_DO_NOT_REMOVE    
		static void Main() {
			Random rnd=new Random();

			for(int i=0; i<100; i++) {
				double[] lx=new double[4];
				double[] ly=new double[4];

				for(int j=0; j<3; j++) {
					lx[j]=2*rnd.NextDouble()-1.0;
					ly[j]=2*rnd.NextDouble()-1.0;
				}
				lx[3]=1;
				ly[3]=1;

				Vector<double> a=CreateVector.Dense(lx);
				Vector<double> b=CreateVector.Dense(ly);

				if((a-b).L2Norm()<epsilon) {
					continue;
				}

				Vector<double> x=direction(a, b);
				Vector<double> z=a-b;
				Trace.Assert(Math.Abs(z*x+z.L2Norm())<epsilon);
			}
		}
		#endif
    }
}
