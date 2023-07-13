lar=float(input('Largura da parede: '))
alt=float(input('Altura da parede: '))
a=lar*alt
l=a/2
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m²'.format(lar,alt,a))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(l))