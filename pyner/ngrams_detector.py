#encoding=utf-8

from java.io import ByteArrayInputStream
from java.util import ArrayList

from org.ppbw.agh.swat.hoover.smith.lexer import HtmlLexer, IResourceLexer
from org.ppbw.agh.swat.hoover.smith.quantum import QuantumType
from org.ppbw.agh.swat.hoover.smith.quantum.detection import DetectedQuantum, DetectorType, IQuantumDetector
from org.ppbw.agh.swat.hoover.smith.resourceModel import IContentSegment, IResourceModel
from org.ppbw.agh.swat.hoover.smith.stemmer import StemmerPL


#from unittest import main, TestCase

ngrams_before = ['']
ngrams_after = ['']
f = open("ngrams.dat", "r")
content = f.read()
before, after = content.split("--")
f.close()
ngrams_before = before.split()
ngrams_after = after.split()

class NgramsDetector(IQuantumDetector):
    def getType(self):
        return DetectorType.DetectionInLeafSegment

    def detectQuantums(self, leafSegment):
        dq = {}
        for word_id in range(1, leafSegment.getWordsCount() - 1):
            prev_word = leafSegment.getWordToken(word_id - 1).tokenContent
            next_word = leafSegment.getWordToken(word_id + 1).tokenContent
            for ngram in ngrams_before:
                if ngram in prev_word:
                    dq[word_id] = DetectedQuantum(leafSegment.getWordToken(word_id), QuantumType.SURNAME)
            for ngram in ngrams_after:
                if ngram in next_word:
                    dq[word_id] = DetectedQuantum(leafSegment.getWordToken(word_id), QuantumType.SURNAME)
        return ArrayList(dq.values())
