nome = str(input('Digite seu nome completo: ')).strip() #serve para retirar os espaços

print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' '))) #esta tirando os espaços
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
divi = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(divi[0], len(divi[0])))