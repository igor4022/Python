from math import factorial

n = int(input('Escolha um número para executar a conta do fatorial...'))
fatoria = factorial(n)

cores = {'limpa':'\033[m',
         'vermelho':'\033[1;31m',}

print('O seu número em {}fatorial{} fica {}{}'.format(cores['vermelho'], cores['limpa'], cores['vermelho'], fatoria))
