using System;
/*
M24

Kirjoita funktio rotate_around_point(alpha, point, X), joka kiertää alpha:n verran homogeenisia
koordinaatteja X pisteen point ympäri vastapäivään. point on paikkavektori. 
Funktio palauttaa muunnetut pisteet matriisissa. Kaikki pisteet ovat R^2 pisteitä, jotka on
upotettu homogeeniseen koordinaatistoon.
*/
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;

namespace Lineaarialgebra
{
    class MyProgram {
		public static Matrix<double> rotate_around_point(double alpha, Vector<double> point, Matrix<double> X) {
			//Your code here
		}
	    #if !TEST_FLAG_DO_NOT_REMOVE    
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

				Matrix<double> Z=rotate_around_point(a, point, X);
				for(int j=0; j<N; j++) {
					Vector<double> x=X.Column(j);
					Vector<double> z=Z.Column(j);
					//Check center of rotation
					Trace.Assert(Math.Abs((point-x).L2Norm()-(point-z).L2Norm())<epsilon);
					//Check rotation angle
					double b=Math.Acos((x-point)*(z-point)/((z-point).L2Norm()*(z-point).L2Norm()));
					Trace.Assert(Math.Abs(Math.Cos(b)-Math.Cos(a))<epsilon);
				}
			}
		}
		#endif
    }
}
