v=float(input('Digite um valor: '))
#import math (importa a biblioteca inteira).
from math import trunc #importa só o método trunc
print('O valor digitado foi {} e sua porção inteira é {}'.format(v,trunc(v)))
#ou print('O valor digitado foi {} e sua porção inteira é {}'.format(v,int(v)))