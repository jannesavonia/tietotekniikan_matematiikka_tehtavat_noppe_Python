using System;
using System.Collections.Generic;
/*
M05

Toteuta alla oleviin funktiopohjiin transpositiosalaus. Modulin
pääohjelmaan on toteutettu testi, jonka avulla voit testata
ja suunnitella toteutustasi.

1) Salaamaton viesti voi sisältää mitä tahansa merkkejä
2) Viestiä ei esikäsitellä millän tavoin ennen salausta
3) Salaus lisää alkuperäisen viestin loppuun tarvittavan määrän välilyöntejä
4) Oikealla avaimella purettu viesti on identtinen alkuperäisen
   salaamattoman viestin kanssa lukuun ottamatta edellä loppuun lisättyjä
   välilyöntejä
5) Avain on int-taulukko, ei tuple, kuten luentokalvoissa on esitetty
*/

using System.Diagnostics;

namespace Lukuteoria
{
    class MyProgram
    {
		
		//Palauttaa salatun vietin, K=avain, M=salattava viesti
		public static string E(ref int[] K, string M) {
			//Your code here

			return C;
		}

		//Palauttaa salaamattoman vietin, K=avain, C=salattu viesti
		public static string D(ref int[] K, string C) {
			//Your code here
        
		    return M;
		}

		#if !TEST_FLAG_DO_NOT_REMOVE    
		static void Main() {
    		string M="tama viesti on salattu transpositiosalauksella";
    		int[] K=new int[]{3, 6, 7, 4, 2, 1, 5};
    		Console.WriteLine($"M = \"{M}\"");
    		Console.WriteLine($"K = {K}");

    		string C=E(ref K, M);
    		Console.WriteLine($"C = \"{C}\"");
    
    		string M_received=D(ref K, C);
    		Console.WriteLine($"M_received = \"{M_received}\"");

    		Trace.Assert(C=="v taiamo einstta ltsanaurs titpiooskusasal  ea ll");
    		int lM=M.Length;
    		Trace.Assert(M_received.Substring(0, lM)==M);
		}
		#endif
    }
}
