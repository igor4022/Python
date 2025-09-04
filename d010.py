lar = float(input('Coloque o valor da largura da sua pareda em M...'))
alt = float(input('Coloque o valor da altura da sua pareda em M...'))

men = lar * alt
res = men / 200

print('O total de tinta que será necessário é de {}L (pensando que 1 balde de tinta pinta uma área de 2m²)'.format(res))