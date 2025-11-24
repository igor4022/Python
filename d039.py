nota1 = float(input('Digite sua primeira nota...'))
nota2 = float(input('Digite sua segunda nota...'))
resul = (nota1 + nota2) / 2

cores = {'verde':'\033[32m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',}

if resul < 5.0:
    print('{}REPROVADO'.format(cores['vermelho']))
elif resul == 5.0 or resul <= 6.9:
    print('{}RECUPERAÇÃO'.format(cores['amarelo']))
else:
    print('{}APROVADO'.format(cores['verde']))