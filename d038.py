from datetime import date

nasci = int(input('Qual ano você nasceu?...'))
hoje = date.today()
ano = hoje.year
resul = ano - nasci
restam = 18 - resul

cores = {'azul':'\033[34m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',}

if resul < 18:
    print('sua idade é {}{}{}, {}você ainda não precisa se alistar, restam {} anos para você'.format(cores['verde'], resul, cores['verde'], cores['azul'], restam))
elif resul < 48:
    print('sua idade é {}{}{}, {}já esta na hora de se alistar a {} anos atras'.format(cores['verde'], resul, cores['verde'], cores['amarelo'], restam))
else:
    print('{}Você não pode mais se alistar '.format(cores['vermelho'], restam))