import random

num = random.randint(1,10)
chute = int(input('Escolha um número de 1 a 10...'))
cores = {'vermelho':'\033[0;31m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verde':'\033[0;32m'}

if num == chute:
    print('{}PARABÉNS!!!{}'.format(cores['verde'], cores['amarelo']))
else:
    print('{}ERROUUU!!!{}'.format(cores['vermelho'], cores['amarelo']))
print('FIM')