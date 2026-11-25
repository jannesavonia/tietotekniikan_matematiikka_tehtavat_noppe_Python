using System;
/*
M14

Laajenna Vect-luokkaa siten että vektorin voi kertoa liukuluvulla. Katso esimerkki
tarvittaessa testiohjelmasta.

Kopioi edellisen tehtävän Vect-luokka tähän pohjaksi.
*/

/*
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
*/
using System.Diagnostics;

namespace Lineaarialgebra
{
	class Vect {
		//Your Vect code here

		static public Vect operator *(double a, Vect b) {
			//Your code here
		}
	};

    #if !TEST_FLAG_DO_NOT_REMOVE    
    class MyProgram
    {
		static void Main() {
    		double[] l1={-0.5, 1};
    		double[] l2={-1.5, -0.8};
    		double a=3.1;
    		double b=-0.7;
    
    		var v1=new Vect(l1);
    		var v2=new Vect(l2);

    		Vect a_times_v1=a*v1;
    		Vect b_times_v2=b*v2;

    		Console.WriteLine($"{a}*{v1}={a_times_v1}");
    		Console.WriteLine($"{b}*{v2}={b_times_v2}");

    		//Test +, -, and []
    		double delta=0.01;
    		for(int i=0; i<l1.Length; i++) {
        		Trace.Assert(Math.Abs(a*l1[i]-a_times_v1[i])<delta);
        		Trace.Assert(Math.Abs(b*l2[i]-b_times_v2[i])<delta);
			}
		}
    }
	#endif
}
