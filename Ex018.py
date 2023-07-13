import math
#from math import radians, sin, cos, tan importa todos os metodos necessarios, depos tirar o "math." da sintaxe
an=float(input('Digite o ângulo que você deseja: '))
se= math.sin(math.radians(an)) #metodo radians serve para converter em graus radianos
co= math.cos(math.radians(an))
tg= math.tan(math.radians(an))
print('O ângulo de {:.1f} tem SENO de {:.2f} \nO ângulo de {:.1f} tem COSSENO de {:.2f} \nO ângulo de {:.1f} tem TANGENTE de {:.2f}'.format(an,se,an,co,an,tg))