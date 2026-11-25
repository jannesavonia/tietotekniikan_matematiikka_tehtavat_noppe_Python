using System;
/*
M30

Ratkaise P'(t) = P(t)*(1-P(t)), kun P(0)=1/2
aikavälillä 0...10s. Tallenna arvot tasasekunteina tiedostoon.

*/
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;
using System.IO;
using MathNet.Numerics.Data.Text;

namespace Lineaarialgebra
{
    class MyProgram {
		static string filename=Path.Combine(Path.GetDirectoryName(new System.Diagnostics.StackTrace(true).GetFrame(0).GetFileName()), "output.txt");

		static double f(double t, double P) {
    		return P*(1-P); 
		}

		static void Main() {
			//Your code here

			//Test code below
			Matrix<double> data = DelimitedReader.Read<double>(filename, false, " ", false);
			Console.WriteLine(data);

			Trace.Assert(data.RowCount==11); //'Length of data error
			Trace.Assert(Math.Abs(data[0, 1]-0.5)<=0.00001); //Accuracy error
			Trace.Assert(Math.Abs(data[3, 1]-0.95257413)<=0.00001); //Accuracy error
			Trace.Assert(Math.Abs(data[10, 1]-0.9999546)<=0.00001); //Accuracy error
		}
    }
}
