sal=float(input('Qual é o salário do Funcionario? R$'))
rea= sal+((sal*15)/100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, \npassa a receber R${:.2f}'.format(sal,rea))