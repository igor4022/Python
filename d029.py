num = int(input('Escolha um número...'))
cores = {'verde':'\033[32m',
         'vermelha':'\033[31m',
         'branco':'\033[m'}

if num % 2 == 0:
    print('Seu número {}{}{} é {}PAR!'.format(cores['verde'], num, cores['branco'], cores['verde']))
else:
    print('Seu número {}{}{} é {}IMPAR!'.format(cores['vermelha'], num, cores['branco'], cores['vermelha']))