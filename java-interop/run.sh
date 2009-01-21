#CLASSPATH=$CLASSPATH:./egothor.jar:./detectors.jar:./morfologik-stemming.jar jython test.py
CLASSPATH=$CLASSPATH:detectors.jar:jython.jar:egothor.jar:morfologik-stemming.jar javac jyinterface/factory/JythonFactory.java
CLASSPATH=$CLASSPATH:detectors.jar:jython.jar:egothor.jar:morfologik-stemming.jar javac Main.java
CLASSPATH=$CLASSPATH:detectors.jar:jython.jar:egothor.jar:morfologik-stemming.jar java Main
#CLASSPATH=$CLASSPATH:./egothor.jar:./detectors.jar:./morfologik-stemming.jar jython research.py

#CLASSPATH=$CLASSPATH:./egothor.jar:./detectors.jar:./morfologik-stemming.jar javac javasucks/Main.java 
#CLASSPATH=$CLASSPATH:./egothor.jar:./detectors.jar:./morfologik-stemming.jar java javasucks.Main
