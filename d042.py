altura = float(input('Qual a sua altura?...'))
peso = float(input('Qual o seu peso?...'))
imc = peso / (altura * 2)

cores = {'amarelo': '\033[33m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',}

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('{}O seu peso está ideal'.format(cores['verde']))
elif imc >= 25 and imc < 30:
    print('{}Você está sobrepeso'.format(cores['azul']))
elif imc >= 30 and imc < 40:
    print('{}Você está obeso'.format(cores['amarelo']))
else:
    print('{}Você está com obesidade mórbida'.format(cores['vermelho']))