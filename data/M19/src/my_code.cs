using System;
/*
M19

Kirjoita funktio perpendicular, joka saa parametrinaan 
kaksi vektoria ja palauttaa True jos ne ovat kohtisuorassa
(jollain sopivalla tarkkuudella)

Vektorin normin saat laskettua esimerkiksi np.linalg.norm-funktiolla
*/
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;

namespace Lineaarialgebra
{
    class MyProgram {
		public static bool perpendicular(Vector<double> a, Vector<double> b) {
			//Your code here
		}

	    #if !TEST_FLAG_DO_NOT_REMOVE    
		static void Main() {
    		Vector<double> v1=CreateVector.Dense(new double[] {0.01, 0.01, 0.01, 0.01});
    		Vector<double> v2=CreateVector.Dense(new double[] {1.0e-6, 2.0e-6, 1.0e-6, -4.0e-6});
    		Vector<double> v3=CreateVector.Dense(new double[] {-40, 20, 20, 0});
    		Vector<double> v4=CreateVector.Dense(new double[] {4, -2, -2, 0});
    		Vector<double> v5=CreateVector.Dense(new double[] {4.0e6, -2.0e6, 4.0e6, 1.0e6});

			Trace.Assert(perpendicular(v1, v2));
			Trace.Assert(perpendicular(v1, v3));
			Trace.Assert(perpendicular(v1, v4));
			Trace.Assert(perpendicular(v2, v5));
			Trace.Assert(perpendicular(v2, v1));
			Trace.Assert(perpendicular(v3, v1));
			Trace.Assert(perpendicular(v4, v1));
			Trace.Assert(perpendicular(v5, v2));
			Trace.Assert(perpendicular(v1, -v2));
			Trace.Assert(perpendicular(-v1, v3));
			Trace.Assert(perpendicular(v1, -v4));
			Trace.Assert(perpendicular(-v2, v5));
			Trace.Assert(perpendicular(v2, -v1));
			Trace.Assert(perpendicular(-v3, v1));
			Trace.Assert(perpendicular(v4, -v1));
			Trace.Assert(perpendicular(-v5, v2));
			Trace.Assert(! perpendicular(v2, v3));
			Trace.Assert(! perpendicular(v3, v4));
			Trace.Assert(! perpendicular(v1, v5));
			Trace.Assert(! perpendicular(v1, v1));
			Trace.Assert(! perpendicular(v2, v2));
			Trace.Assert(! perpendicular(v3, v3));
			Trace.Assert(! perpendicular(v4, v4));
			Trace.Assert(! perpendicular(v5, v5));
			Trace.Assert(! perpendicular(v1, -v1));
			Trace.Assert(! perpendicular(v2, -v2));
			Trace.Assert(! perpendicular(v3, -v3));
			Trace.Assert(! perpendicular(v4, -v4));
			Trace.Assert(! perpendicular(v5, -v5));
		}
		#endif
    }
}
