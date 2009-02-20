:mod:`pyner.detectors` -- Detektory zgodne ze SWAT 
==================================================
.. module:: pyner.detectors

.. function:: gen_detector(detector)

Funkcja tworzy obiekt zgodny z interfejsem 
`org.ppbw.agh.swat.hoover.smith.quantum.detection.IQuantumDetector` na
podstawie reguły w formie funkcji.


.. class:: NgramsNeighboursDetector

Detektor utworzony na podstawie reguły :func:`pyner.rules.ngrams_neighbours`


.. class:: PrefixesDetector

Detektor utworzony na podstawie reguły :func:`pyner.rules.prefixes`


.. class:: SuffixesDetector

Detektor utworzony na podstawie reguły :func:`pyner.rules.suffixes`


.. class:: CorpusDetector

Detektor utworzony na podstawie reguły :func:`pyner.rules.in_name_corpus`


.. class:: CapitalDetector

Detektor utworzony na podstawie reguły :func:`pyner.rules.starts_with_capital`


.. class:: CombinedDetector

Detektor kombinowany, zwracający jedynie te wyniki, które znajdują się w
odpowiedziach więcej niż połowy reguł prostych.


.. class:: CombinedDetector2

Detektor kombinowany, podobny do :class:`CombinedDetector`, lecz obniżający
nieco próg wejścia (wymagana zgodność jedynie z 1/3 reguł). Podnosi to pokrycie
kosztem dokładności odpowiedzi.


.. class:: SmartDetector

Detektor kombinowany, korzystający z reguł prostych w bardziej wyszukany
sposób. Niektóre reguły są traktowane jako pewne dopasowania (np. obecność w
korpusie nazwisk nie posiadających znaczenia jako słowa), inne jako pewne
ograniczenia (słowa nie wykrytę przez regułę wielkich liter na pewno nie będą
nazwiskami). Pozostałe reguły są kombinowane tak jak w
:class:`CombinedDetector`.


