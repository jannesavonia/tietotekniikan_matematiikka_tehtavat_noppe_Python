using System;
using System.Collections.Generic;
/*
M08

Toteuta funktio phi(n), joka palauttaa Eulerin funktion arvon n:lle. 

Jos käytät muiden tehtävien ratkaisuja, niin kopio funktiot tähän
tiedostoon. Älä käytä niitä moduleina.
*/

using System.Diagnostics;

namespace Lukuteoria
{
    class MyProgram
    {
		public static ulong phi(ulong n, bool visual=false) {
			//Your code here
		}
		#if !TEST_FLAG_DO_NOT_REMOVE    
		static void Main() {
			    Trace.Assert(phi(10)==4);
    			Trace.Assert(phi(1)==1);
    			Trace.Assert(phi(16)==8);
    			Trace.Assert(phi(90)==24);
    			Trace.Assert(phi(101)==100);
    			Trace.Assert(phi(3)==2);
		}
		#endif
    }
}
