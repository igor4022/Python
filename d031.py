
ano = int(input('Digite o ano de nascimento..'))
cores = {'verde':'\033[32m',
         'vermelha':'\033[31m'}

if ano % 4 == 0:
    print('O ano é {}BISSEXTO!'.format(cores['verde']))
else:
    print('O seu ano não é {}BISSEXTO!'.format(cores['vermelha']))
