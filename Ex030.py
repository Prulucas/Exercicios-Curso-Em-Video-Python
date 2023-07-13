num = int(input('\033[0;35mMe diga um número qualquer: \033[m'))
if num == 0:
    print('O número 0 é par')
elif num % 2 ==0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é impar'.format(num))