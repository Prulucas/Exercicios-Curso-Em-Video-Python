from time import sleep
print('-='*15)
print('Analisador de Triângulo...')
print('-='*15)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
sleep(2)
if a < b + c and b < a +c and c < a + b:
    print('\033[0;32mOs segmentos acima PODEM formar um triângulo!')
else:
    print('\033[0;31mOs segmentos acima NÃO PODEM formar um triângulo')
