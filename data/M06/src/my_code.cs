using System;
using System.Collections.Generic;
/*
M06

Toteuta funktio syt(a, b), joka palauttaa a:n ja b:n suurimman yhteisen tekijän. 
*/

using System.Diagnostics;

namespace Lukuteoria
{
    class MyProgram
    {
		public static ulong syt(ulong a, ulong b) {
    		//Your code here
		}
	    #if !TEST_FLAG_DO_NOT_REMOVE    
		static void Main() {
			Trace.Assert(syt(100, 35)==5);
			Trace.Assert(syt(35, 100)==5);
			Trace.Assert(syt(10, 35)==5);
			Trace.Assert(syt(21, 14)==7);
			Trace.Assert(syt(3, 21)==3);
			Trace.Assert(syt(3, 3)==3);
			Trace.Assert(syt(2, 62)==2);
			Trace.Assert(syt(13, 17)==1);
			Trace.Assert(syt(12378, 3054)==6);
		}
		#endif
    }
}
