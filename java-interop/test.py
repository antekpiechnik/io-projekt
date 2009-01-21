#encoding=utf-8

from os.path import abspath, dirname
from java.io import ByteArrayInputStream
import jreload

from org.ppbw.agh.swat.hoover.smith.lexer import HtmlLexer, IResourceLexer
from org.ppbw.agh.swat.hoover.smith.quantum import QuantumType
from org.ppbw.agh.swat.hoover.smith.quantum.detection import DetectedQuantum, DetectorType, IQuantumDetector
from org.ppbw.agh.swat.hoover.smith.resourceModel import IContentSegment, IResourceModel
from org.ppbw.agh.swat.hoover.smith.stemmer import StemmerPL


from unittest import main, TestCase


class InternetDetector(IQuantumDetector):
    def getType(self):
        return DetectorType.DetectionInLeafSegment

    def detectQuantums(self, leafSegment):
        dq = []
        for word_id in range(leafSegment.getWordsCount()):
            if leafSegment.compareWord(word_id, "Internet"):
                dq.append(DetectedQuantum(leafSegment.getWordToken(word_id), QuantumType.NICKNAME))
                print leafSegment.getWordToken(word_id).tokenContent
        return dq


class InternetDetectorTest(TestCase):
    def test_all(self):
        html = u"<p>ale Internet, normalnie internet, <p> a Internetek i Internet, że szkoda gadać..."
        is_ = ByteArrayInputStream(html.encode("utf-8"))
        lexer = HtmlLexer()
        stemmer = StemmerPL()
        resourceModel = lexer.buildResourceModel(is_, "utf-8", stemmer)
        bd = InternetDetector()
        dqs = []
        for s in resourceModel.getLeafSegments():
            dqs.extend(bd.detectQuantums(s))

        true_len = len(dqs)
        self.assertEquals(2, true_len)

if __name__ == "__main__":
    main()
