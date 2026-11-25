using System;
/*
M31

Toteuta solver(T). Katso tarkempi tehtävä luentokalvoista. 
*/
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;
using System.IO;
using MathNet.Numerics.Data.Text;

namespace Lineaarialgebra
{
    class MyProgram {
		static string filename=Path.Combine(Path.GetDirectoryName(new System.Diagnostics.StackTrace(true).GetFrame(0).GetFileName()), "output.txt");
		
		static public void solver(double T) {
				//Your code here
				//Sample output to file
				//outputFile.WriteLine($"{t_i} {x[0]} {x[1]}");
		}
	    #if !TEST_FLAG_DO_NOT_REMOVE    
		static void Main() {
			solver(20);

    		double eps=0.01;
			Matrix<double> data = DelimitedReader.Read<double>(filename, false, " ", false);
			Console.WriteLine(data);

			for(int idx=0; idx<data.RowCount; idx++) {
				double t=data[idx, 0];
				Trace.Assert(Math.Abs(idx-t)<0.001); //Sould be saved on integer t
				double x_computed=data[idx, 1];
				double y_computed=data[idx, 2];
        		double x_correct=2.0*Math.Cos(t);
        		double y_correct=2.0*Math.Sin(t);

        		Vector<double> diff=CreateVector.Dense(new double[]{x_computed-x_correct, y_computed-y_correct});
				double diff_norm=diff.L2Norm();
        		Console.WriteLine($"{t}, {x_correct}, {x_computed}, {y_correct}, {y_computed}, [{diff[0]}, {diff[1]}], {diff_norm}");
        		Trace.Assert(diff_norm<eps);
			}
		}
		#endif
    }
}
