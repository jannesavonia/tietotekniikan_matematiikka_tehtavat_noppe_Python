using System;
/*
M22

Kirjoita funktio unitnormal(a, b), jossa a ja b ovat R^3:n vektoreita 
(ei homogeenisissa koordinaateissa). Funktio palauttaa a:n ja b:n virittämän tason 
yksikkönormaalin, eli yksikkövektorin, joka on molempia vektoreita vasten kohtisuorassa.
*/
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;
using MathNet.Spatial.Euclidean;

namespace Lineaarialgebra
{
    class MyProgram {
		static public Vector<double> unitnormal(Vector<double> a, Vector<double> b) {
			//Your code here!
			//HINT: MathNet.Spatial.Euclidean contains Vector3D class, which contains CrossProduct method
		} 

	    #if !TEST_FLAG_DO_NOT_REMOVE    
		static void Main() {
			double epsilon=0.0001;
			Random rnd=new Random();

			for(int i=0; i<500; i++) {
				Vector<double> a=CreateVector.Dense(new double[] {rnd.NextDouble(), rnd.NextDouble(), rnd.NextDouble()});
				Vector<double> b=CreateVector.Dense(new double[] {rnd.NextDouble(), rnd.NextDouble(), rnd.NextDouble()});

				if(a.L2Norm()<epsilon || b.L2Norm()<epsilon) {
					continue;
				}

				Vector<double> normal=unitnormal(a, b);
				Vector<double> minus_normal=unitnormal(b, a);

				//Check that a x b = -b x a
				Trace.Assert((normal+minus_normal).L2Norm()<epsilon);
				Trace.Assert(Math.Abs(a*normal)<epsilon);
				Trace.Assert(Math.Abs(b*normal)<epsilon);
				Trace.Assert(Math.Abs(normal.L2Norm()-1)<epsilon);
			}
		}
		#endif
    }
}
