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
		String shortName = "org.ppbw.agh.swat.hoover.smith.quantum.detection.IQuantumDetector";
		Object obj = JythonFactory.getJythonObject(shortName, "pyner/trivial_detector.py", "InternetDetector");
		IQuantumDetector detector = (IQuantumDetector) obj;
		HtmlLexer lexer = new HtmlLexer();
		IResourceModel resourceModel = 
			lexer.buildResourceModel(new ByteArrayInputStream("Internet Internet internet ze szkoda gadać".getBytes("UTF-8")), 
						 "utf-8",
						 new StemmerPL());

		for (IContentSegment s : resourceModel.getLeafSegments()) {
			System.out.println(detector.detectQuantums(s).toString());
		}
	}
}
