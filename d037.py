numero1 = int(input('Escolha um número...'))
numero2 = int(input('Escolha mais um número...'))

cores = {'azul':'\033[34m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'limpa':'\033[m',}

if numero1 > numero2:
    print('ao seu {}primeiro númerom {}{} é maior qur o seu {}segundo número {}'.format(cores['amarelo'], numero1, cores['limpa'], cores['azul'], numero2))
elif numero1 < numero2:
    print('O seu {}segundo número {}{} é maior que o seu {}primeiro número {}'.format(cores['azul'], numero2, cores['limpa'], cores['amarelo'], numero1))
else:
    print('{}Os dois números são iguais'.format(cores['vermelho']))