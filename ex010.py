nome = str(input('Qual é seu nome?...'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'pretoebranco':'\033[7;30m',}

if nome == 'Igor':
    print('{}Que nome bonito!'.format(cores['azul']))
    print('{}Bom dia {}{}!{}'.format(cores['azul'], cores['amarelo'], nome, cores['azul']))

elif nome =='Pedro'  or nome == 'Maria' or nome == 'Paulo':
    print('{}Seu nome é bem popular no Brasil!...'.format(cores['vermelho']))
else:
    print('{}Seu nome é bem comun...'.format(cores['verde']))
print('{}Tenha um bom dia {}{}!'.format(cores['limpa'], cores['amarelo'], nome))