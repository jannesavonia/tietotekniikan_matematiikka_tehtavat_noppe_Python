using System;
using System.Collections.Generic;
/*
M09

Toteuta alla olevaan pohjaan modulaariaritmetiikan toteuttava luokka (omat toteutukset kummallekin)

1) +,-,* operaattorit toimivat myös kun oikealla puolella on kokonaisluku
2) Osa koodista on valmiiksi kirjoitettu, älä muokkaa sitä
3) Toteuta luokka niin, etta luvun a mod n a:lle pätee 0<=a<n.

*/

using System.Diagnostics;
using System;
using System.Numerics;


namespace Lukuteoria
{
	class Mod {
		private long a;
		private ulong n;

		//Apufunktio pow-metodin toteuttamiseksi 
	    static ulong modpow(ulong a, ulong b, ulong n) {
			return (ulong)BigInteger.ModPow(a, b, n);
    	}
		public Mod(long a_, ulong n_) {
			n=n_;
			a=((a_%(long)n)+(long)n)%(long)n; //To make sure that 0<=a<n
		}

		//Malliksi toteutettu + operaattori
		public static Mod operator +(Mod a, Mod b) {
			if(a.n!=b.n) {
				throw new ArgumentException("a.n!=b.n");
			}
			return new Mod(a.a+b.a, a.n);
		}

		//Malliksi toteutettu + operaattori
		public static Mod operator +(Mod a, int b) {
			return new Mod(a.a+b, a.n);			
		}

		public static Mod operator -(Mod a, Mod b) {
			//Your code here
		}

		public static Mod operator -(Mod a, int b) {
			//Your code here
		}

		public static Mod operator *(Mod a, Mod b) {
			//Your code here
		}

		public static Mod operator *(Mod a, int b) {
			//Your code here
		}

		public static bool operator ==(Mod a, Mod b) {
			//Your code here
		}

		public static bool operator ==(Mod a, int b) {
			//Your code here
		}

		// != operaattori annettuna valmiiksi, koska C# vaatii sen
		public static bool operator !=(Mod a, Mod b) {
			return !(a.a==b.a);
		}

		public static bool operator !=(Mod a, int b) {
			var bb=new Mod(b, a.n);
			return !(a==b);			
		}



		//Malliksi toteutettu ToString()
		public override string ToString() {
			return $"({a} mod {n})";
		}

		//Malliksi toteutettu ToLong()
		public long ToLong() {
			return a;
		}

		public Mod pow(ulong k) {
			//Your code here
		}

	}
    class MyProgram
    {
	    #if !TEST_FLAG_DO_NOT_REMOVE    
		static void Main() {
			Mod a_1_6=new Mod(1, 6);
    		Mod a_17_6=new Mod(17, 6);
    		Mod b_1_5=new Mod(1, 5);
    		Mod b_11_5=new Mod(11, 5);

		    //Test exception if a.n!=b.n
    		string error="";
			try {
		        Mod c=a_1_6+b_1_5;
        		error="No exception with Mod(1,6)+Mod(1,5)";
			} catch {
				//pass
			}
			Trace.Assert(error=="");
		    
			error="";
			try {
		        Mod c=a_1_6-b_1_5;
        		error="No exception with Mod(1,6)-Mod(1,5)";
			} catch {
				//pass
			}
			Trace.Assert(error=="");

			error="";
			try {
		        Mod c=a_1_6*b_1_5;
        		error="No exception with Mod(1,6)*Mod(1,5)";
			} catch {
				//pass
			}
			Trace.Assert(error=="");

			//Test + operator and ToString()
			Trace.Assert((a_1_6+a_17_6).ToString()=="(0 mod 6)");
			Trace.Assert((b_1_5+b_11_5).ToString()=="(2 mod 5)");

    		//Test +, *, -, and == operator
    		Mod d_6=a_17_6*5;
			Mod zz=new Mod(1, 6);
    		Trace.Assert(d_6==zz);

    		d_6=(a_17_6+a_1_6)*a_17_6;
			zz=new Mod(0, 6);
    		Trace.Assert(d_6==zz);

    		d_6=(a_17_6-a_1_6)*a_17_6;
			zz=new Mod(2, 6);
    		Trace.Assert(d_6==zz);

    		Mod d_5=b_11_5.pow(4);
			zz=new Mod(1, 5);
    		Trace.Assert(d_5==zz);

			d_5=(b_1_5+b_11_5).pow(5);
			zz=new Mod(2, 5);
    		Trace.Assert(d_5==zz);
    		Trace.Assert(d_5.ToLong()==2);
    		Trace.Assert(b_11_5.ToLong()==1);
		}
		#endif
    }
}
