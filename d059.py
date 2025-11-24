import random

n1 = int(input('Escolha um número...'))
n2 = int(input('Escolha mais um ultimo...'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',}

val = random.randint(1,5)
res = int(input('''{}MUITO BOM!{}

Agora escolha que tipo de calculo você quer fazer:

{}[1]: soma
{}[2]: multiplicar
{}[3]: dividir
{}[4]: novos números
{}[5]: sair

{}ESCOLHA...'''.format(cores['amarelo'], cores['limpa'],cores['verde'], cores['azul'], cores['amarelo'], cores['limpa'], cores['vermelho'], cores['limpa'])))

if res == 1:
    soma = n1 + n2
    print('Os números {}{}{} e {}{} somados{}, vai dar o resultado igual {}{}'.format(cores['verde'], n1, cores['limpa'], cores['verde'], n2, cores['limpa'], cores['verde'], int(soma)))
elif res == 2:
    multi = n1 * n2
    print('Os números {}{}{} e {}{} multiplicados{}, vai dar o resultado igual {}{}'.format(cores['azul'], n1, cores['limpa'], cores['azul'], n2, cores['limpa'], cores['azul'], int(multi)))
elif res == 3:
    divi = n1 / n2
    print('Os números {}{}{} e {}{} divididos{}, vai dar o resultado {}{}'.format(cores['amarelo'], n1, cores['limpa'], cores['amarelo'],n2, cores['limpa'], cores['amarelo'], int(divi)))
elif res == 4:
    print('Apénas resete o progama')
elif res == 5:
    print('{}Aperte o botão de reiniciar o progama'.format(cores['vermelho']))
else:
    print('{}----- !!!ERRADO!!! -----{}'.format(cores['vermelho'], cores['limpa']))
    res = int(input('Tente de NOVO...'))

    if res == 1:
        soma = n1 + n2
        print('Os números {}{}{} e {}{} somados{}, vai dar o ressultad igual {}{}'.format(cores['verde'], n1, cores['limpa'], cores['verde'], n2, cores['limpa'], cores['verde'], int(soma)))
    elif res == 2:
        multi = n1 * n2
        print('Os números {}{}{} e {}{} multiplicados{}, vai dar o resultado igual {}{}'.format( cores['azul'], n1, cores['limpa'], cores['azul'], n2, cores['limpa'], cores['azul'], int(multi)))
    elif res == 3:
        divi = n1 / n2
        print('Os números {}{}{} e {}{} divididos{}, vai dar o resultado {}{}'.format(cores['amarelo'], n1, cores['limpa'], cores['amarelo'], n2, cores['limpa'], cores['amarelo'], int(divi)))
    elif res == 4:
        print('Apénas reste o progama')
    elif res == 5:
        print('{}Aperte o botão de reiniciar o progama'.format(cores['vermelho']))
    else:
        print('FIM')
