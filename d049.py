n1 = int(input('Digite um valor...'))

cores = {'azul': '\033[1;34m',
         'amarelo': '\033[1;33m',
         'limpa': '\033[m', }

for cont in range(0, 11):
    print('{}{}{}x{}{}{}={}{}'.format(cores['azul'], n1, cores['limpa'], cores['azul'], cont, cores['limpa'], cores['amarelo'], n1 * cont))