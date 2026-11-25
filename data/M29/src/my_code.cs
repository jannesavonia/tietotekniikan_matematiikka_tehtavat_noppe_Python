using System;
/*
M29
Raketin massa on 100kg ja sen moottorin työntövoima on 2000N. Oletetaan, että
alkunopeus ja -paikka ovat molemmat 0. Raketti ammuttaan suoraan ylöspäin siten,
että moottori on aluksi päällä 1s ja sitten pois päältä saman ajan käynnistyen taas 1s
ajaksi jne. 

Kirjoita ohjelma, joka simuloi raketin lentokorkeutta ajan funktiona. Ohjelma tallentaa
tiedostoon output.txt raketin korkeuden ajanhetkinä t=0, 1, 2...10 (sekuntia). Tiedoston 
ensimmäinen sarake sisältää ajan (sekunteina) ja toinen korkeuden (metreinä).
Yksiköitä ei talleteta tiedostoon. Sarakkeet erotetaan välilyönnillä. Käytä 
gravitaatiokiihtyvyydelle arvoa g=10m/s^2 ja jätetään ilmanvastus huomioimatta.

Valitse tehtävään sopiva menetelmä. Raketin korkeus millä tahansa ajanhetkellä
saa erota todellisesta arvosta enintään 0.1m.
*/
using System.Diagnostics;
using MathNet.Numerics.LinearAlgebra;
using System.IO;
using MathNet.Numerics.Data.Text;

namespace Lineaarialgebra
{
    class MyProgram {
		const double g=10;//m/s*2
		// filename="src/output.txt"
		static string filename=Path.Combine(Path.GetDirectoryName(new System.Diagnostics.StackTrace(true).GetFrame(0).GetFileName()), "output.txt");


		static void Main() {
			//Your code here
			//Sample file output:
			//outputFile.WriteLine($"{t} {z[0]}");


			//Test code below
			Matrix<double> data = DelimitedReader.Read<double>(filename, false, " ", false);
			Console.WriteLine(data);

			Trace.Assert(data.RowCount==11); //'Length of data error
			Trace.Assert(Math.Abs(data[0, 1]-0.0)<=0.1); //Accuracy error
			Trace.Assert(Math.Abs(data[1, 1]-5.0)<=0.1); //Accuracy error
			Trace.Assert(Math.Abs(data[10, 1]-50.0)<=0.1); //Accuracy error
		}
    }
}
