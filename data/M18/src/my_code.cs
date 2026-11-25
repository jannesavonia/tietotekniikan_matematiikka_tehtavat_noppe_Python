using System;
/*
M18

Lisää Vect-luokkaan projektion laskeva funktio proj(v), joka
laskee vektorin projektion v:lle. Jos dimensiot eivät täsmää,
niin heitetään poikkeus.

Kopioi edellisen tehtävän Vect-luokka tähän pohjaksi.
*/
using System.Diagnostics;

namespace Lineaarialgebra
{
	class Vect {
		//Kopioi koodi tähän

		public Vect proj(Vect v) {
			//Your code here
		}
	};
    #if !TEST_FLAG_DO_NOT_REMOVE    
    class MyProgram
    {
		static void Main() {
			double[] l1=new double[] {1, 1, 1, 1};
			double[] l2=new double[] {1, 2, 1, -3};
			double[] l3=new double[] {-4, 2, -2, 0};

			Vect v1=new Vect(l1);
			Vect v2=new Vect(l2);
			Vect v3=new Vect(l3);

			Vect p_v2_v1=v2.proj(v1); //v2 projektio v1:lle
    		Vect p_v2_v3=v2.proj(v3);
    		Vect p_v1_v3=v1.proj(v3);

    		double delta=0.01;
    		Trace.Assert(((v1*v1)*p_v2_v1-(v1*v2)*v1).norm()<delta);
    		Trace.Assert(((v3*v3)*p_v2_v3-(v3*v2)*v3).norm()<delta);
    		Trace.Assert(((v3*v3)*p_v1_v3-(v3*v1)*v3).norm()<delta);
		}
    }
	#endif
}
