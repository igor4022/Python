import random

num = random.randint(1, 10)
esc = int(input('Tente adivinhar o número que o computador esta pensando...'))

cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',}

while num != esc:
   print('{}--- ERROU FEI ERROU RUDE!!! ---{}'.format(cores['vermelho'], cores['limpa']))
   esc = int(input('tente de novo meu filho!...'))

else:
    print('{}!!!PARABENZ!!!{}'.format(cores['amarelo'], cores['limpa']))
    print('O número que o robô estava pensando era {}{}{}.'.format(cores['azul'], num, cores['limpa']))
    str(input('E você sabe qual é´o seu premio!...'))
    print('{}!!!EZATAMENTE!!!{}...............................................................................{}NADA!'.format(cores['amarelo'], cores['limpa'], cores['amarelo']))
