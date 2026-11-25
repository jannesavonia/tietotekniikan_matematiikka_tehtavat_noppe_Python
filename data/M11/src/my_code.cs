using System;
using System.Collections.Generic;
/*
M11

Toteuta funktio keys(p, q, e, n, d), joka palauttaa julkisen ja yksityisen avaimen
RSA-salaukseen. Parametrit n ja d ovat paluuarvoja.

Palautetut avaimet ovat Kpub=(n, e) ja Kpriv=(n, d), jossa n, e, d ovat positiivisia
kokonaislukuja.

Jos käytät aiempien tehtävien ratkaisuja, niin kopio lähdekoodit tähän 
tiedostoon. Älä koeta käyttää niin moduleina.
*/

using System.Diagnostics;
using System.Numerics;

namespace Lukuteoria
{
    class MyProgram
    {

		public static void keys(ulong p, ulong q, ulong e, ref ulong n, ref ulong d) {
			//Your code here
		}

	    #if !TEST_FLAG_DO_NOT_REMOVE    
		static void Main() {
			ulong n=0;
			ulong d=0;
			ulong e=0;

			e=7;
			keys(17, 13, e, ref n, ref d);
			var Kpub=(n, e);
			var Kpriv=(n, d);
			//Console.WriteLine(Kpub);
			//Console.WriteLine(Kpriv); 
    		Trace.Assert(Kpub==(221, 7));
    		Trace.Assert(Kpriv==(221, 55));

			e=3;
			try {
				keys(17, 13, e, ref n, ref d);
				Console.WriteLine("ERROR: syt(13-1, 3)=3, exception not generated!");
				Trace.Assert(false);
			} catch {
				//Console.WriteLine("Got exception, ok...");
				//Test went ok...
			}

			e=17;
			keys(12601, 6043, e, ref n, ref d);
			Kpub=(n, e);
			Kpriv=(n, d);
			//Console.WriteLine(Kpub);
			//Console.WriteLine(Kpriv);
    		Trace.Assert(Kpub==(76147843, 17));
    		Trace.Assert(Kpriv==(76147843, 17912753));
		}
		#endif
    }
}
