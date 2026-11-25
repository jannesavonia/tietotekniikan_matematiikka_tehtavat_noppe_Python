using System;
/*
M17

Lisää Vect-luokkaan pistetulo. Käytä pistetulon operaattorina *.
Jos vektoreiden dimensiot eivät ole samat, heitetään poikkeus.

Kopioi edellisen tehtävän Vect-luokka tähän pohjaksi.
*/
using System.Diagnostics;

namespace Lineaarialgebra
{
	class Vect {
		//Kopioi Vect-luokka edellisestä tehtävästä tähän
	
		static public double operator *(Vect a, Vect b) {
			//Your code here
		}
	};
    #if !TEST_FLAG_DO_NOT_REMOVE    
    class MyProgram
    {
		static void Main() {
			double[] l1=new double[] {1, 1, 1, 1};
			double[] l2=new double[] {-2, 2, 3, -3};
			double[] l3=new double[] {-1, 2, -2, 0};

			Vect v1=new Vect(l1);
			Vect v2=new Vect(l2);
			Vect v3=new Vect(l3);

			//Testataan pistetulo
    		double delta=0.01;
    		Trace.Assert(Math.Abs(v1*v2-0)<delta);
			Trace.Assert(Math.Abs(v1*v1-4)<delta);
			Trace.Assert(Math.Abs(v2*v2-26)<delta);
			Trace.Assert(Math.Abs(v3*v2-0)<delta);
			Trace.Assert(Math.Abs(v3*v1-(-1))<delta);
		}
    }
	#endif
}
