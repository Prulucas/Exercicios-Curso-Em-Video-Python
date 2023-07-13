dis = float(input('Qual é a distância da sua viagem? '))
if dis <= 200:
    preço = dis * 0.5
    print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(dis))
    print('E o preço da sua passagem será de R${:.2f}'.format(preço))
else:
    preço = dis * 0.45
    print('Você está prestes a começar uma viagem de {:.1f}Km'.format(dis))
    print('E o preço da sua passagem será de R${:.2f}'.format(preço))
