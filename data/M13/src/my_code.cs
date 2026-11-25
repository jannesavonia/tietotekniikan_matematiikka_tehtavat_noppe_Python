using System;
/*
M13

Toteuta luokka Vect, joka osaa vektoreiden yhteen- ja vähennyslaskun.
Vektorin arvo annetaan muodostimen list-tyyppeisenä parametrina.
Mikäli laskutoimitusta yritetään vektoreille, joiden dimensio ei ole
sama, niin heitetään poikkeus. Lisäksi toteutetaan []-operaattori, joka palauttaa
vektorin alkion ja toimii kuten list-tyypin vastaava operaattori. Indeksointi alkaa 0:sta. 
Toteuta lisäksi ToStr-funktio, joka tulostaa vektorin muodossa [1, 2.3, 4, -1.2], siis
samoin kuin esimerkiksi list-tyyppi.
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
		double[] items;

		public Vect(double[] v) {
			items=(double[])v.Clone();
		}

		static public Vect operator+(Vect a, Vect b) {
			//Your code here
		}

		static public Vect operator-(Vect a, Vect b) {
			//Your code here
		}

		public override string ToString() {
			string s="[";
			for(int i=0; i<items.Length; i++) {
				s+=items[i];
				if(i<items.Length-1) {
					s+=", ";
				}
			}
			s+="]";
			return s;
		}

		public double this[int index] {
			get { return items[index]; }
			set { items[index] = value; }
        }
	};

    #if !TEST_FLAG_DO_NOT_REMOVE    
    class MyProgram
    {
		static void Main() {
    		double[] l1={-0.5, 1};
    		double[] l2={-1.5, -0.8};
    
    		var v1=new Vect(l1);
    		var v2=new Vect(l2);

    		var v1_plus_v2=v1+v2;
    		var v1_minus_v2=v1-v2;
			Console.WriteLine($"{v1}+{v2}={v1_plus_v2}");
    		Console.WriteLine($"{v1}-{v2}={v1_minus_v2}");
		}
    }
	#endif
}
