# Aprēķināt riņķa līnijas garumu, ja tiek ievadīts tās rādiuss.
from math import pi
r = float(input ("Ievadi rinka linijas radiusu, lai apreikinatu garumu : "))
print ("Rinka linijas garums ar " + str(r) + " ir: " + str(pi * r**2))
