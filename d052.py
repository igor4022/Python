num = int(input('Escolha um numero...'))

cores = {'azul':'\033[1;34m',
         'amarelo':'\033[1;33m', }

if num % 2 == 0:
    print('Seu número é {}PAR'.format(cores['azul']))
else:
    print('Seu número é {}IMPAR'.format(cores['amarelo']))