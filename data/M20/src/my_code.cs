using System;
/*
M20

Kirjoita funktio projection(x, y), joka palauttaa x:n
projektion y:lle. Jos y on 0-vektori, niin heitetään poikkeus.
*/
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;

namespace Lineaarialgebra
{
    class MyProgram {
		static double epsilon=0.0001;

		public static Vector<double> projection(Vector<double> x, Vector<double> y) {
			//Your code here
		}

	    #if !TEST_FLAG_DO_NOT_REMOVE    
		public static void check(Vector<double> x, Vector<double> y, ref bool perp, ref bool dir) {
			        Vector<double> proj=projection(x, y);
        			perp=(Math.Abs((x-proj)*y)<epsilon);
        			dir=(Math.Abs(Math.Abs(y*proj)-(y.L2Norm()*proj.L2Norm()))<epsilon);

		}
		static void Main() {
			Random rnd=new Random();

			for(int i=3; i<30; i++) {
				Console.WriteLine("-------------------------------------------------");
				double[] lx=new double[i];
				double[] ly=new double[i];

				for(int j=0; j<i; j++) {
					lx[j]=2*rnd.NextDouble()-1.0;
					ly[j]=2*rnd.NextDouble()-1.0;
				}

				Vector<double> x=CreateVector.Dense(lx);
				Vector<double> y=CreateVector.Dense(ly);
				Console.WriteLine($"x={x}");
				Console.WriteLine($"y={y}");

				bool perp=false;
				bool dir=false;

				check(x, y, ref perp, ref dir);

        		Trace.Assert(perp); //'x-Px was not perpendicular to y'
        		Trace.Assert(dir);  //'||Px|| was not correct, or Px was not parallel to y'

			}
		}
		#endif
    }
}
