using System;
using System.Collections.Generic;
/*
M07

Toteuta funktio sieve(N), joka palauttaa listan, jossa on alkuluvut <=N.

Vihje:
1) tee taulukko P, joka sisältää luvut 0..N
2) aseta poistetut numerot taulukossa 0:ksi
3) aseta luku 1 taulukossa 0:ksi
4) tee lista taulukosta
*/

using System.Diagnostics;

namespace Lukuteoria
{
    class MyProgram
    {
		public static List<ulong> sieve(ulong N) {
			//Your code here

			return Plist;
		}
	    #if !TEST_FLAG_DO_NOT_REMOVE    
		static void Main() {
			List<ulong> primes=sieve(1000000);
			Trace.Assert(primes.Count==78498);
			Trace.Assert(primes.Contains(99391));
			Trace.Assert(primes.Contains(999983));
			Trace.Assert(primes.Contains(2));
			Trace.Assert(primes.Contains(3));
			Trace.Assert(!primes.Contains(4));
			Trace.Assert(!primes.Contains(99837));
		}
		#endif
    }
}
