using System;
using System.Collections.Generic;
/*
M12

Toteuta RSA-salauksen salaus- ja purkufunktio alle. Avaimet ovat Kpub=(n, e)
ja Kpriv=(n, d), jossa n, e, d ovat kokonaislukuja, sekä M<n ja C<N 
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
		public static ulong E(ulong n, ulong e, ulong M) {
			//Your code here
		}

		public static ulong D(ulong n, ulong d, ulong C) {
			//Your code here
		}

	    #if !TEST_FLAG_DO_NOT_REMOVE    
		static void Main() {
    		var Kpub=((ulong)221, (ulong)7);
    		var Kpriv=((ulong)221, (ulong)55);
			ulong M=197;
			ulong C=E(Kpub.Item1, Kpub.Item2, M);
			Trace.Assert(C==141);
			ulong Mreceived=D(Kpriv.Item1, Kpriv.Item2, C);
			Trace.Assert(Mreceived==M);

			Kpub=((ulong)76147843, (ulong)17);
    		Kpriv=((ulong)76147843, (ulong)17912753);
			M=2525417;
			C=E(Kpub.Item1, Kpub.Item2, M);
			Trace.Assert(C==66511275);
			Mreceived=D(Kpriv.Item1, Kpriv.Item2, C);
			Trace.Assert(Mreceived==M);
		}
		#endif
    }
}
