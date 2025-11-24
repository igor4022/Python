from datetime import  date

nascimento = int(input('Em que ano você nasceu?...'))
hoje = date.today()
ano = hoje.year
idade = ano - nascimento

cores = {'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'vermelho': '\033[31m',
         'branco': '\033[m',}

if idade <= 9:
    print('Parabéns, sua idade é {}{}{} ou seja você é da liga {}MIRIM!'.format(cores['verde'], idade, cores['branco'], cores['verde']))
elif idade <= 14:
    print('Parabéns, sua idade é {}{}{} ou seja você é da liga {}INFANTIL!'.format(cores['azul'], idade, cores['branco'], cores['azul']))
elif idade <= 19:
    print('Parabéns, sua idade é {}{}{} ou seja você é da liga {}JUNIOR!'.format(cores['roxo'], idade, cores['branco'],cores['roxo']))
elif idade <= 20:
    print('Parabéns, sua idade é {}{}{} ou seja você é da liga {}SENIOR!'.format(cores['amarelo'], idade, cores['branco'], cores['amarelo']))
else:
    print('Parabéns, sua idade é {}{}{} ou seja você é da liga {}MASTER!'.format(cores['vermelho'], idade, cores['branco'], cores['vermelho']))