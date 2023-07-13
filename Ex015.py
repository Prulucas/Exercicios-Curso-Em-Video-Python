al=int(input('Quantos dias alugados? '))
km=float(input('Quantos Km rodados? '))
dias= al * 60
kmr= km * 0.15
tot= dias + kmr
print('O total a pagar é de R${:.2f}'.format(tot))