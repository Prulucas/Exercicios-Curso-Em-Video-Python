fr = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes na frase.'.format(fr.count('a')))
print('A primeira letra A apareceu na posição {}'.format(fr.find('a')+1))
print('A ultima letra A apareceu na posição {}'.format(fr.rfind('a')+1))