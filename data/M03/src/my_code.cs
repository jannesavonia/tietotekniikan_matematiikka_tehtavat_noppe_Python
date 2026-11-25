using System;
using System.Collections.Generic;
using System.Diagnostics;
/*
M03

Toteuta alla oleviin funktiopohjiin substituutiosalaus. Modulin
pääohjelmaan on toteutettu testi, jonka avulla voit testata
ja suunnitella toteutustasi.

1) Salaamaton viesti sisältää kirjaimia a-z tai A-Z sekä välilyöntejä
   ja muita erikoismerkkejä
2) Kaikki kirjaimet muutetaan isoiksi kirjaimiksi ennen salausta
3) Välilyönnit ja erikoismerkit jätetään sellaisenaan salattuun viestiin
4) Oikealla avaimella purettu viesti on identtinen alkuperäisen
   salaamattoman viestin kanssa, lukuun ottamatta sitä, että kaikki
   kirjaimet ovat muuttuneet isoiksi.
5) Avain on sanakirja (dict/Dictionary), jonka avain kuvautuu salauksessa vastaavaksi arvoksi.
   Esimerkiksi alla olevassa avaimessa A kuvautuu K:ksi ja D kuvautuu L:ksi.
   Purettaessa salausta tapahtuu tietenkin päinvastainen, eli K kuvautuu A:ksi ja
   L kuvautuu D:ksi. 
*/


namespace Lukuteoria
{
    class MyProgram
    {
		
		//Palauttaa salatun vietin, K=avain, M=salattava viesti
		public static string E(ref Dictionary<char, char> K, string M) {
			//Your code here
			
			return C;
		}

		//Palauttaa salaamattoman vietin, K=avain, C=salattu viesti
		public static string D(ref Dictionary<char, char> K, string C) {
			//Your code here
			
			return M;
		}

	    #if !TEST_FLAG_DO_NOT_REMOVE    

		static void Main() {
			string M="Et osaa murtaa tata!";
			var K= new Dictionary<char, char>() {
				{'A', 'K'},
				{'B', 'B'},
				{'C', 'N'},
				{'D', 'L'},
				{'E', 'M'},
				{'F', 'A'},
				{'G', 'O'},
				{'H', 'F'},
				{'I', 'G'},
				{'J', 'H'},
				{'K', 'W'},
				{'L', 'X'},
				{'M', 'Y'},
				{'N', 'Z'},
				{'O', 'P'},
				{'P', 'Q'},
				{'Q', 'T'},
				{'R', 'U'},
				{'S', 'R'},
				{'T', 'E'},
				{'U', 'S'},
				{'V', 'V'},
				{'W', 'C'},
				{'X', 'I'},
				{'Y', 'D'},
				{'Z', 'J'}
			};
			
			Console.WriteLine($"M = \"{M}\"");
			Console.WriteLine($"K = \"{K}\"");

			var C=E(ref K, M);
			Console.WriteLine($"C = \"{C}\"");
			
			var M_received=D(ref K, C);
			Console.WriteLine($"M_received = \"{M_received}\"");

			Trace.Assert(C=="ME PRKK YSUEKK EKEK!");
			Trace.Assert(M_received==M.ToUpper());
		}
		#endif
    }
}
