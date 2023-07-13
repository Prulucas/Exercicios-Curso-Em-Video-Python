from random import randint
from time import sleep
computador = randint(0,5)
print('\033[0;33m -=- {}'*20)
print('\033[0;34m Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[0;33m -=- \033[m'*20)
num = int(input('Em que número eu pensei? '))
print('\033[0;35m PROCESSANDO... \033[m')
sleep(2)

if num == computador:
    print('\033[0;32m PARABÉNS! Você conseguiu me vencer!')
else:
    print('\033[0;31m GANHEI! Eu pensei no número {}'.format(computador))