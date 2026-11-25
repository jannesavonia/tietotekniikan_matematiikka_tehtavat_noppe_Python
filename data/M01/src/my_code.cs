using System;
/*
M01

Toteuta alla oleviin funktiopohjiin Caesar-salaus. Modulin
pääohjelmaan on toteutettu testi, jonka avulla voit testata
ja suunnitella toteutustasi.

1) Salaamaton viesti sisältää kirjaimia a-z tai A-Z sekä välilyöntejä
   ja muita erikoismerkkejä
2) Kaikki kirjaimet muutetaan isoiksi kirjaimiksi ennen salausta
3) Välilyönnit ja erikoismerkit jätetään sellaisenaan salattuun viestiin
4) Oikealla avaimella purettu viesti on identtinen alkuperäisen
   salaamattoman viestin kanssa, lukuun ottamatta sitä, että kaikki
   kirjaimet ovat muuttuneet isoiksi.
*/

/*
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
*/
using System.Diagnostics;

namespace Lukuteoria
{
    class MyProgram
    {
	const int N_ALPHABETS=26;
	
	//Palauttaa salatun vietin, K=avain, M=salattava viesti
	public static string E(int K, string M) {
	    //Your code here

	    return C;
	}

	//Palauttaa salaamattoman vietin, K=avain, C=salattu viesti
	public static string D(int K, string C) {
	    //Your code here
	    
	    return M;
	}

    #if !TEST_FLAG_DO_NOT_REMOVE    
		static void Main() {
			string M="Et osaa murtaa tata!";
			int K=16;
			Console.WriteLine("M="+"'"+M+"'");
			Console.WriteLine("K="+"'"+K.ToString()+"'");

			var C=E(K, M);
			Console.WriteLine("C="+"'"+C+"'");
		
			var M_received=D(K, C);
			Console.WriteLine("M_received="+"'"+M_received+"'");
			Trace.Assert(M.ToUpper()==M_received.ToUpper());

			Console.WriteLine("Test passed");
		}
	#endif
    }
}
