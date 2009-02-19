package agh.io;

import org.ppbw.agh.swat.hoover.smith.quantum.detection.IQuantumDetector;
import jyinterface.factory.JythonFactory;
import org.ppbw.agh.swat.hoover.smith.lexer.HtmlLexer; 
import org.ppbw.agh.swat.hoover.smith.lexer.IResourceLexer; 
import org.ppbw.agh.swat.hoover.smith.quantum.detection.DetectedQuantum; 
import org.ppbw.agh.swat.hoover.smith.resourceModel.IContentSegment; 
import org.ppbw.agh.swat.hoover.smith.resourceModel.IResourceModel; 
import org.ppbw.agh.swat.hoover.smith.stemmer.StemmerPL; 
import java.io.ByteArrayInputStream; 

public class Main {
	public static void main(String[] args) throws Exception {

        String text = "Hrabia Napoleon Stanisław Adam Feliks Zygmunt Krasiński herbu Ślepowron (ur. 19 lutego 1812 w Paryżu – zm. 23 lutego 1859 w Paryżu) – jeden z najwybitniejszych poetów polskiego romantyzmu." + 
"Tradycyjnie Krasińskiego zwykło zaliczać się do grona tzw. Czterech Wieszczów literatury polskiej (obok Adama Mickiewicza, Juliusza Słowackiego i Cypriana Kamila Norwida), choć coraz częstsze są próby zdetronizowania Krasińskiego przez współczesną krytykę literacką." + 
"Był potomkiem magnackiej rodziny Krasińskich II ordynatem opinogórskim, synem generała Wincentego i Marii Radziwiłłówny. Jego ojcem chrzestnym był cesarz Napoleon I." + 
"" + 
"Dzieciństwo i młodość" + 
"Kształcił się w domu w Warszawie i Opinogórze, pod kierunkiem pisarza Józefa Korzeniowskiego, później w Liceum Warszawskim i na wydziale prawa Uniwersytetu Warszawskiego do roku 1829. Z powodu zajścia z kolegą Leonem Łubieńskim na tle wyłamania się Krasińskiego spod solidarności koleżeńskiej z okazji patriotycznej demonstracji na pogrzebie prezesa Sądu Sejmowego Piotra Bielińskiego, ojciec wysłał go do Szwajcarii." + 
"Gdy wyjechał do Szwajcarii, zapoznał się tam z literaturą i myślą europejskiego romantyzmu. Największy wpływ na jego poglądy i całe życie miał ojciec, Wincenty Krasiński – generał napoleoński, zwolennik 'obozu klasyków', a później lojalny poddany cara Rosji. Zygmunt stracił matkę w 1822 roku. Mimo buntu, młodego jeszcze poety, nigdy nie udało mu się wyrwać spod wpływu ojca, który ingerował zarówno w jego poglądy polityczne, jak i życie osobiste (np. wymusił małżeństwo z Elizą Branicką, mimo miłości poety do Delfiny Potockiej). Krasiński pod wpływem ojca nie wziął udziału w powstaniu listopadowym i demonstracjach patriotycznych. Poddany ostracyzmowi kolegów zmuszony był przerwać studia. Od połowy maja do września 1857 r. przebywał w Złotym Potoku, z którego wyjechał po śmierci swojej najmłodszej córki. Uciekł z ojczyzny, aby choćby częściowo uwolnić się spod wpływu ojca. Odtąd przebywa przeważnie za granicą w: Niemczech, Francji i Włoszech." + 
"W roku 1829 w Genewie poznał się i zaprzyjaźnił z Anglikiem Henrykiem Reeve (korespondencję z nim wydał Józef Kallenbach, 1902, 2 tomy) i z Henrietą Villan, drugą swą miłością, po poprzednim, młodzieńczym uczuciu do kuzynki Amelii Załuskiej. W sierpniu 1830 roku spotkał się z Adamem Mickiewiczem, z którym odbył wycieczkę w Alpy. Po roku 1831 nawiedzały go stale cierpienia fizyczne, rozstrój nerwowy, potęgowany różnicą przekonań politycznych w stosunku do ojca, dla którego był jednak uległym synem, oraz najprzykrzejsza, stale go już trapiąca choroba oczu, grożąca ślepotą, zniewalająca do długiego nieraz przebywania w ciemnym pokoju i do samotnych rozmyślań. Od jesieni 1832 do wiosny 1833 przebywał w Petersburgu z ojcem, który chciał go nakłonić do służby dla dworu rosyjskiego, ale temu żądaniu ojca się nie poddał. Po Krakowie, który go zachwycił historyczną przeszłością, i Wiedniu, gdzie leczył oczy, udał się do Włoch, gdzie w Rzymie w roku 1834 nawiązał stosunek miłosny z Joanną Bobrową, który trwał do 1838. Stałym jego towarzyszem w tych podróżach był dawny kolega uniwersytecki Konstanty Danielewicz. W roku 1836 w Rzymie poznał Juliusza Słowackiego i zaprzyjaźnił się z nim." + 
"W grudniu 1838 roku w Neapolu nawiązał romans z Delfiną Potocką, najsilniejsze z uczuć poety, gorąco odwzajemniane. Stosunek miłosny przetrwał do roku 1846, później przekształcił się w przyjaźń i wydatnie odbił się w twórczości poety. W roku 1839 w Mediolanie zaprzyjaźnił się z Augustem Cieszkowskim, była to najtrwalsza i najściślejsza z przyjaźni poety i wzajemnie wywarła wpływ na dzieje myśli ich obu (korespondencję wydał Józef Kallenbach, 1912, 2 tomy). W lipcu 1843 roku pod wpływem ojca ożenił się z Elizą Branicką (1820-1876), polską malarką i dyletantką, której uczucie i zalety charakteru ocenił dopiero później, gdy ochłódł jego stosunek z Delfiną.";

		String shortName = "org.ppbw.agh.swat.hoover.smith.quantum.detection.IQuantumDetector";
        String[] detectorNames = { "NgramsNeighboursDetector", "PrefixesDetector", "SuffixesDetector", "CorpusDetector",
				"CapitalDetector", "CombinedDetector", "CombinedDetector2", "SmartDetector"};
        for (String detectorName : detectorNames) {
            Object obj = JythonFactory.getJythonObject(shortName, "pyner/ngrams_detector.py", detectorName);
            IQuantumDetector detector = (IQuantumDetector) obj;
            HtmlLexer lexer = new HtmlLexer();
            IResourceModel resourceModel =
                lexer.buildResourceModel(new ByteArrayInputStream(text.getBytes("UTF-8")),
                             "utf-8",
                             new StemmerPL());

            System.out.println(detectorName + ":");
            for (IContentSegment s : resourceModel.getLeafSegments()) {
                for (DetectedQuantum dq : detector.detectQuantums(s)) {
                    System.out.println("  " + dq.quantum.getContent());
                }
            }
        }
	}
}
