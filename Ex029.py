vel = int(input('Qual é a velocidade atual do carro? '))
if vel >= 80:
    print('\033[0;31mMULTADO! Você excdeu o limite permitido que é de 80Km/h')
    mul = (vel - 80) * 7
    print('Você deve pagar uma multa e {:.2f}!'.format(mul))
else:
    print('\033[0;32mDentro do limite permitido!')
print('\033[0;33mTenha um bom dia! Dirija com segurança!\033[m')