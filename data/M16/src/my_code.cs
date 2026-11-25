using System;
/*
M16

Lisää Vect-luokkaan funktio unit(), joka palauttaa vektorin kanssa
samansuuntaisen yksikkövektorin. Mikäli vektori on 0-vaktori,
niin heitetään poikkeus.

Kopioi edellisen tehtävän Vect-luokka tähän pohjaksi.
*/
using System.Diagnostics;

namespace Lineaarialgebra
{
	class Vect {
		//Kopioi Vect-luokka tänne
		
		public Vect unit() {
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


    		Vect u1=v1.unit();
    		Vect u2=v2.unit();

    		double delta=0.01;
    		double norm_u1=u1.norm();
    		double norm_u2=u2.norm();

    		//Testataan, että on yksikkövektori
    		Trace.Assert(Math.Abs(1-norm_u1)<delta);
    		Trace.Assert(Math.Abs(1-norm_u2)<delta);
    
    		//Testataan, että saatu vektori on samansuuntainen kuin alkuperäinen vektori
    		Vect uu1=v1.norm()*u1;
    		Trace.Assert((v1-uu1).norm()<delta);
    		Vect uu2=v2.norm()*u2;
    		Trace.Assert((v2-uu2).norm()<delta);

    		//Testataan, että 0-vektori aiheuttaa poikkeuksen
			double[] l0=new double[] {0, 0, 0};
   			Vect v0=new Vect(l0);
    		try {
        		Vect u0=v0.unit();
        		Console.WriteLine("Exception failed");
				return;
			} catch {
				//Exception generated, ok...
			}
		}
    }
	#endif
}
