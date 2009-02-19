from java.io import ByteArrayInputStream
from java.util import ArrayList
from java.lang import System

from org.ppbw.agh.swat.hoover.smith.lexer import HtmlLexer, IResourceLexer
from org.ppbw.agh.swat.hoover.smith.quantum import QuantumType
from org.ppbw.agh.swat.hoover.smith.quantum.detection import DetectedQuantum, DetectorType, IQuantumDetector
from org.ppbw.agh.swat.hoover.smith.resourceModel import IContentSegment, IResourceModel
from org.ppbw.agh.swat.hoover.smith.stemmer import StemmerPL

from sets import Set as set
from pyner import rules


def gen_detector(rule):
    class Detector(IQuantumDetector):
        def getType(self):
            return DetectorType.DetectionInLeafSegment

        def detectQuantums(self, leafSegment):
            words = [leafSegment.getWordToken(word_id).tokenContent for word_id in range(leafSegment.getWordsCount())]
            return ArrayList([DetectedQuantum(leafSegment.getWordToken(wid), QuantumType.SURNAME) for wid in rule(words)])
    return Detector

NgramsNeighboursDetector    = gen_detector(rules.ngrams_neighbours)
PrefixesDetector            = gen_detector(rules.prefixes)
SuffixesDetector            = gen_detector(rules.suffixes)
CorpusDetector              = gen_detector(rules.in_name_corpus)
CapitalDetector             = gen_detector(rules.starts_with_capital)
