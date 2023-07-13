pre=float(input('Qual é o preço do produto? R$'))
des=pre-((pre*5)/100)
print('O produto que custava R${:.2f}, \nna promoção com desconto de 5% passa a custar R${:.2f}'.format(pre,des))