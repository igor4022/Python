import random

esc = int(input('''Faça sua escolha:
                   *Escolha 1 para pedra
                   *Escolha 2 para papel
                   *Escolha 3 para tesoura
                   Digite aqui...'''))

jok = ['pedra', 'papel', 'tesoura']
res = random.choice(jok)

cores = {'azul': '\033[34m',
         'vermelho': '\033[31m',
         'branco': '\033[m',}

if esc == 1:
    print('O computador escolheu {}{}{} e você escolheu {}pedra'.format(cores['vermelho'], res, cores['branco'], cores['azul']))
elif esc == 2:
    print('O computador escolheu {}{}{} e você escolheu {}papel'.format(cores['vermelho'], res, cores['branco'], cores['azul']))
elif esc == 3:
    print('O computador escolheu {}{}{} e você escolheu {}tesoura'.format(cores['vermelho'], res, cores['branco'], cores['azul']))