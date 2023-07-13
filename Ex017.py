import math
'''from math import hypot'''
cco=float(input('Comprimento do cateto oposto: '))#comprimento do cateto oposto
cca=float(input('Comprimento do cateto adjacente: '))#comprimento do cacateto adjacente
#ch= ((cca**2) + (cco**2)) ** (1/2)#comprimento da hipotenusa
'''print('A hipotenusa vai edir {:.2f}'.format(ch)) maneira matemática sem import'''

ch= math.hypot(cco,cca)
print('A hipotenusa vai medir {:.2f}'.format(ch))