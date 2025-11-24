from datetime import date

cores = {'amarelo': '\033[33m',
         'limpa': '\033[m',}

for const in range (1, 7):
    nasci = int(input('Qual ano você nasceu...'))
    data = date.today()
    ano = data.year
    resul = ano - nasci

    if  resul >= 18:
        print('Você tem {}{}{} anos de idade, você está na {}maior idade!{}'.format(cores['amarelo'], resul, cores['limpa'], cores['amarelo'], cores['limpa']))
    else:
        print('Você tem {}{}{} anos de idade, você {}não{} está na {}maior idade!{}'.format(cores['amarelo'], resul, cores['limpa'], cores['amarelo'], cores['limpa'], cores['amarelo'], cores['limpa'] ))