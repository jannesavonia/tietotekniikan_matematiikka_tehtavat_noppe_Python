using System;
/*
M15

Lisää Vect-luokkaan vektorin normin palauttava metodi norm(). Katso esimerkki
tarvittaessa testiohjelmasta.

Lisää myös staattinen metodi dist(a, b), joka palauttaa
pisteiden a ja b välisen etäisyyden. a ja b ovat pisteiden paikkavaktoreita. 
Katso esimerkki tarvittaessa testiohjelmasta.

Kopioi edellisen tehtävän Vect-luokka tähän pohjaksi.
*/
using System.Diagnostics;

namespace Lineaarialgebra
{
	class Vect {
		//Kopioi Vect luokka tähän

		public double norm() {
			//Your code here
		}

    	static public double dist(Vect a, Vect b) {
			//Your code here
		}
	};

    #if !TEST_FLAG_DO_NOT_REMOVE    
    class MyProgram
    {
		static void Main() {
			double[] l1=new double[] {1, 1, 1, 1};
			double[] l2=new double[] {0.3, 0.4};
			double a=3.1;
			double b=-0.7;

			Vect v1=new Vect(l1);
			Vect v2=new Vect(l2);

			double len1=2.0;
			double a_len1=Math.Abs(a)*len1;
			double len2=0.5;
			double b_len2=Math.Abs(b)*len2;

			double delta=0.01;

			//Normin laskenta
			double norm_v1=v1.norm();
			Trace.Assert(Math.Abs(len1-norm_v1)<delta);
			Trace.Assert(Math.Abs(a_len1-(a*v1).norm())<delta);
			Trace.Assert(Math.Abs(len2-v2.norm())<delta);
			Trace.Assert(Math.Abs(b_len2-(b*v2).norm())<delta);

			l1=new double[] {0.5, 0.1};
			l2=new double[] {0.3, 0.4};
			Vect p1=new Vect(l1);
			Vect p2=new Vect(l2);

			double d=0.13;

			//p1 ja p2 etäisyys
			double d_p1_p2=Vect.dist(p1, p2);
			Trace.Assert(Math.Abs(d_p1_p2-Math.Sqrt(d))<delta);
		}
    }
	#endif
}
