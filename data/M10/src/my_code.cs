using System;
using System.Collections.Generic;
/*
M10

Toteuta funktio syt_ext(a, b, x, y), joka palauttaa s, x, y, jossa 
s=syt(a, b) ja 
ax+by=syt(a, b) 
*/

using System.Diagnostics;

namespace Lukuteoria
{
    class MyProgram
    {
		public static ulong syt_ext(ulong a, ulong b, ref long x, ref long y) { //x and y are used to return values
			//Your code here
		}

	    #if !TEST_FLAG_DO_NOT_REMOVE    
		static void Main() {
			long x=0;
			long y=0;
			ulong a=0;
			ulong b=0;
			ulong g=0;

			(a, b)=(100, 35);
    		g=syt_ext(a, b, ref x, ref y);
    		Trace.Assert(g==5);
    		Trace.Assert((long)a*x+(long)b*y-(long)g==0);

			(a, b)=(10, 35);
    		g=syt_ext(a, b, ref x, ref y);
    		Trace.Assert(g==5);
    		Trace.Assert((long)a*x+(long)b*y-(long)g==0);

			(a, b)=(21, 14);
    		g=syt_ext(a, b, ref x, ref y);
    		Trace.Assert(g==7);
    		Trace.Assert((long)a*x+(long)b*y-(long)g==0);

			(a, b)=(3, 21);
    		g=syt_ext(a, b, ref x, ref y);
    		Trace.Assert(g==3);
    		Trace.Assert((long)a*x+(long)b*y-(long)g==0);

			(a, b)=(3, 3);
    		g=syt_ext(a, b, ref x, ref y);
    		Trace.Assert(g==3);
    		Trace.Assert((long)a*x+(long)b*y-(long)g==0);

			(a, b)=(2, 62);
    		g=syt_ext(a, b, ref x, ref y);
    		Trace.Assert(g==2);
    		Trace.Assert((long)a*x+(long)b*y-(long)g==0);

			(a, b)=(13, 17);
    		g=syt_ext(a, b, ref x, ref y);
    		Trace.Assert(g==1);
    		Trace.Assert((long)a*x+(long)b*y-(long)g==0);

			(a, b)=(12378, 3054);
    		g=syt_ext(a, b, ref x, ref y);
    		Trace.Assert(g==6);
    		Trace.Assert((long)a*x+(long)b*y-(long)g==0);
		}
		#endif
    }
}
