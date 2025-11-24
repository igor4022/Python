numero = int(input('Escolha um número inteiro qualquer...'))

binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

cores = {'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',}

opsao = int(input('''
 1 para binario
 2 para octal
 3 para hexadecimal
 Escolha...
 '''))

if  opsao == 1 :
    print('{}O seu número {} em binario fica {}'.format( cores['azul'], numero, binario))
elif opsao == 2:
    print('{}O seu número {} em octal fica {}'.format( cores['amarelo'], numero, octal))
elif opsao == 3:
    print('{}O seu numero {} em hexadecimal fica {}'.format( cores['verde'],numero, hexadecimal))
else:
    print('{}Não é possível executar pois você não escolheu nenhuma das opções disponíveis'.format(cores['vermelho']))