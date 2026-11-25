using System;
/*
M26

v(t)=[-sin t]
     [cos t]

x(0)=[1]
     [0]

Kirjoita funktio euler_circle(Dt, n, filename), joka kirjoittaa tekstitiedostoon filename jokaisella aika-askelella:
    t_i = ajanhetki, ensimmäinen 0 ja viimeinen n*Dt
    x_i = ajanhetkeä vastaava x-koordinaatti
    y_i = ajanhetkeä vastaava y-koordinaatti.
Sarakkeet erotetaan välilyönnillä. Tiedostossa on siis n+1 riviä.

Parametrit:
    Dt = aika-askel
    n = aika-askeleiden lukumäärä

Ratkaisussa käytetään luentokalvoissa esitettyä Euler-menetelmää.
*/
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;
using System.IO;
using MathNet.Numerics.Data.Text;

namespace Lineaarialgebra
{
    class MyProgram {

		static Vector<double> f(double t, Vector<double> x) {
			//Your code here
		}

		static public void euler_circle(double Dt, int n, string filename) {
			//Your code here
			//Example of saving a row into the file:
			//   outputFile.WriteLine($"{t_i} {x_i} {y_i}");

	        }
	    }
	
	    #if !TEST_FLAG_DO_NOT_REMOVE    
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
			double T=19;
    		double dt=0.001;
    		int N=Convert.ToInt32(T/dt);
			string filename="src/output.txt";

    		euler_circle(dt, N, filename);

			Matrix<double> data = DelimitedReader.Read<double>(filename, false, " ", false);
			
			double[,] accurate_values=new double[, ] 	{{3.3, Math.Cos(3.3), Math.Sin(3.3)},
                              							{6.3, Math.Cos(6.3), Math.Sin(6.3)},
                              							{18.9, Math.Cos(18.9), Math.Sin(18.9)}};

			Trace.Assert(data.RowCount==N+1);
			Trace.Assert(data.ColumnCount==3);

			Vector<double> t_col=data.Column(t_col_idx);
			Vector<double> x_col=data.Column(x_col_idx);
			Vector<double> y_col=data.Column(y_col_idx);

			double eps=0.001;
    		Trace.Assert(Math.Abs(t_col.Minimum()-0)<eps);
    		Trace.Assert(Math.Abs(t_col.Maximum()-N*dt)<eps);

			for(int i=0; i<accurate_values.GetLength(0); i++) {
				double t=accurate_values[i, t_col_idx];
				double x=accurate_values[i, x_col_idx];
				double y=accurate_values[i, y_col_idx];
				double dx=0;
				double dy=0;

				compare_xy(data, t, x, y, ref dx, ref dy, dt);

				Trace.Assert(dx<eps); //Check accuracy
				Trace.Assert(dy<eps); //Check accuracy
			}
		}
		#endif
    }
}
