from java.io import ByteArrayInputStream
from java.util import ArrayList
from java.lang import System

from org.ppbw.agh.swat.hoover.smith.lexer import HtmlLexer, IResourceLexer
from org.ppbw.agh.swat.hoover.smith.quantum import QuantumType
from org.ppbw.agh.swat.hoover.smith.quantum.detection import DetectedQuantum, DetectorType, IQuantumDetector
from org.ppbw.agh.swat.hoover.smith.resourceModel import IContentSegment, IResourceModel
from org.ppbw.agh.swat.hoover.smith.stemmer import StemmerPL

from sets import Set as set
from rules import *

ENC = System.getProperty("file.encoding")
f = open("ngrams.dat", "r")
content = f.read()
content = content.decode(ENC)
before, after = content.split("--")
f.close()
BEFORE_NGRAMS = before.split()
AFTER_NGRAMS = after.split()

def ngrams_neighbours(words):
    ret = set()
    for n, word in enumerate(words):
        if n > 0:
            prev_word = words[n - 1]
            for ngram in BEFORE_NGRAMS:
                if ngram in prev_word:
                    ret.add(n)
        if n < len(words) - 1:
            next_word = words[n + 1]
            for ngram in AFTER_NGRAMS:
                if ngram in next_word:
                    ret.add(n)
    return ret


def gen_detector(rule):
    class Detector(IQuantumDetector):
        def getType(self):
            return DetectorType.DetectionInLeafSegment

        def detectQuantums(self, leafSegment):
            words = [leafSegment.getWordToken(word_id).tokenContent for word_id in range(leafSegment.getWordsCount())]
            return ArrayList([DetectedQuantum(leafSegment.getWordToken(wid), QuantumType.SURNAME) for wid in rule(words)])
    return Detector

NgramsDetector = gen_detector(ngrams_neighbours)
