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
            result = [x for x in rule(words) if words[x].strip().isalpha()]
            return ArrayList([DetectedQuantum(leafSegment.getWordToken(wid), QuantumType.SURNAME) for wid in result])
    return Detector

def combine(rules, treshold=0.5):
    def combined_rule(words):
        results = [set(rule(words)) for rule in rules]
        ret = []
        for n in range(len(words)):
            if len([x for x in results if n in x]) > (len(rules) * treshold):
                ret.append(n)
        return ret
    return combined_rule

def smart(words):
    ret = set(rules.in_name_corpus(words))
    ret.update(combine([rules.prefixes, rules.suffixes, rules.ngrams_neighbours])(words))
    obligatory = set(rules.starts_with_capital(words))
    ret = ret & obligatory
    return list(ret)

NgramsNeighboursDetector    = gen_detector(rules.ngrams_neighbours)
PrefixesDetector            = gen_detector(rules.prefixes)
SuffixesDetector            = gen_detector(rules.suffixes)
CorpusDetector              = gen_detector(rules.in_name_corpus)
CapitalDetector             = gen_detector(rules.starts_with_capital)
CombinedDetector            = gen_detector(combine(rules.all))
CombinedDetector2           = gen_detector(combine(rules.all, 0.3))
SmartDetector               = gen_detector(smart)
