sal = float(input('Qual é o salário do funcionário? R$'))
rea = (sal * 10)/100 + sal if sal > 1250 else (sal*15)/100 + sal
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sal,rea))
