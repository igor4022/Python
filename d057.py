sex =  str(input('Digite seu sexo M/F...')).strip().upper()[0]

cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'amarelo': '\033[33m',
    'verde': '\033[32m', }

while sex not in 'MmFf':
    sex = str(input('{}---[INVALIDO]---{}Digite seu sexo M/F...'.format(cores['vermelho'], cores['limpa']))).strip().upper()[0]
else:
    print('{}FIM'.format(cores['amarelo']))