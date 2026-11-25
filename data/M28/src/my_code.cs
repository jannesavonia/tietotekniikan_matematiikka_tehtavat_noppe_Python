using System;
/*
  M28

  x(0)=[1]
       [0]

  v(0)=[0]
       [1]
 
  a(x)=(-1.25/||x||)*x-0.3*v

  Kirjoita funktio ab_spiral(Dt, n, filename), joka tallentaa tekstitiedostoon filename jokaisella aika-askelella:
  t_i = ajanhetki, ensimmäinen 0 ja viimeinen n*Dt
  x_i = ajanhetkeä vastaava x-koordinaatti
  y_i = ajanhetkeä vastaava y-koordinaatti.
  Sarakkeet erotetaan välilyönnillä. Tiedostossa on siis n+1 riviä.

  Parametrit:
  Dt = aika-askel
  n = aika-askeleiden lukumäärä

  Ratkaisussa käytetään luentokalvoissa esitettyä 2. kertaluvun Adams-Bashforth-menetelmää.
  Käynnistä laskenta Eulerin menetelmällä.
*/
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;
using System.IO;
using MathNet.Numerics.Data.Text;
using System.Linq;

namespace Lineaarialgebra
{
	class MyProgram
	{

		static public void ab_spiral(double Dt, int n, string filename)
		{
			using (StreamWriter outputFile = new StreamWriter(filename))
			{
				//Your code here
				//Sample output to file:
				//outputFile.WriteLine($"{t_i} {x[0]} {x[1]}");
			}
		}
		static int t_col_idx = 0;
		static int x_col_idx = 1;
		static int y_col_idx = 2;

		static void compare_xy(Matrix<double> data, double t, double x, double y, ref double dx, ref double dy, double dt)
		{
			dx = 1000000000.0;
			dy = 1000000000.0;
			for (int i = 0; i < data.RowCount; i++)
			{
				Vector<double> row = data.Row(i);
				double t_data = row[t_col_idx];
				if (t_data > t - dt / 2 && t_data < t + dt / 2)
				{
					dx = Math.Abs(x - row[x_col_idx]);
					dy = Math.Abs(y - row[y_col_idx]);
					return;
				}
			}
		}
	    #if !TEST_FLAG_DO_NOT_REMOVE    
		static void Main()
		{
			int N = 100;
			double dt = 10.0 / N;
			string filename = "src/output.txt";

			ab_spiral(dt, N, filename);

			Matrix<double> data = DelimitedReader.Read<double>(filename, false, " ", false);

			double[,] inaccurate_values = new double[,]    {{4.3, 0.3348311043562908, -0.10543010657264017}, 
					{6.7,  -0.025926510426994766, -0.2557111932731299}};

			double[,] accurate_values = new double[,]  {{4.3,  0.33590747680361643, -0.08836541262642196},
					{6.7,  -0.019781308150982085, -0.2621123367635826}};

			Trace.Assert(data.RowCount == N + 1);
			Trace.Assert(data.ColumnCount == 3);

			Vector<double> t_col = data.Column(t_col_idx);
			Vector<double> x_col = data.Column(x_col_idx);
			Vector<double> y_col = data.Column(y_col_idx);

			double eps = 0.0001;
			Trace.Assert(Math.Abs(t_col.Minimum() - 0) < eps);
			Trace.Assert(Math.Abs(t_col.Maximum() - N * dt) < eps);

			for (int i = 0; i < inaccurate_values.GetLength(0); i++)
			{
				double t = inaccurate_values[i, t_col_idx];
				double x = inaccurate_values[i, x_col_idx];
				double y = inaccurate_values[i, y_col_idx];
				double dx = 0;
				double dy = 0;

				compare_xy(data, t, x, y, ref dx, ref dy, dt);

				Trace.Assert(dx < eps); //Check accuracy
				Trace.Assert(dy < eps); //Check accuracy
			}

			N = 10000;
			dt = 10.0 / N;
			ab_spiral(dt, N, filename);
			data = DelimitedReader.Read<double>(filename, false, " ", false);
			for (int i = 0; i < accurate_values.GetLength(0); i++)
			{
				double t = accurate_values[i, t_col_idx];
				double x = accurate_values[i, x_col_idx];
				double y = accurate_values[i, y_col_idx];
				double dx = 0;
				double dy = 0;

				compare_xy(data, t, x, y, ref dx, ref dy, dt);

				Trace.Assert(dx < eps); //Check accuracy
				Trace.Assert(dy < eps); //Check accuracy
			}
		}
		#endif
	}
}
