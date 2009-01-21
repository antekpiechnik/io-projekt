from java.lang import ClassLoader

cl = ClassLoader.getSystemClassLoader().getSystemResource("research.py")
print cl
