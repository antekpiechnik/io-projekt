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

        String text = "Czesław ma w domu kota. Pan Nowak zamieszkały w Lublinie nie lubi tego kota. Roman Giertych zdobywał wiedzę w Oksfordzie. ";

		String shortName = "org.ppbw.agh.swat.hoover.smith.quantum.detection.IQuantumDetector";
        String[] detectorNames = { "NgramsNeighboursDetector", "PrefixesDetector", "SuffixesDetector", "CorpusDetector", "CapitalDetector"};
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
