soma = 0
cont = 0

cores = {'azul': '\033[1;34m',
         'amarelo': '\033[1;33m',
         'limpa': '\033[1;m',}

for c in range(1, 8):
    val =  int(input('Digite {} valor...'.format(c)))
    if val % 2 == 0:
        soma += val
        cont += 1
print('Você escolheu {}{}{} números e o valor somando apenas os números {}PARES{} a {}2{} é {}{}'.format(cores['amarelo'], cont, cores['limpa'], cores['azul'], cores['limpa'], cores['azul'], cores['limpa'], cores['amarelo'], soma))

