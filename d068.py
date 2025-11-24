import random

cores = {'limpa': '\033[m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',}

print(f'''=====> JOGUE {cores['vermelho']}ÍMPAR{cores['limpa']} ou {cores['verde']}PAR{cores['limpa']} com o {cores['amarelo']}COMPUTADOR{cores['limpa']} <=====
-------------------------------------------------''')

res = 0
esc = 0
cont = 0 - 1

while True:
    res = int(input(f'Escolha um número de {cores['verde']}1{cores['limpa']} a {cores['vermelho']}10{cores['limpa']}...'))
    esc = str(input(f'Escolha entre {cores['vermelho']}IMPAR{cores['limpa']} e {cores['verde']}PAR{cores['limpa']}...Digitando {cores['verde']}P{cores['limpa']}/{cores['vermelho']}I{cores['limpa']}...')).strip().upper()[0]
    aleatorio = random.randint(1, 10)
    robot = aleatorio + res
    cont += 1

    if esc in 'Pp' and robot % 2 == 0:
       print(f'{cores['vermelho']}PERDEU{cores['limpa']}')
       break

    elif esc in 'Ii' and robot % 3 == 0:
        print(f'{cores['vermelho']}PERDEU{cores['limpa']}')
        break

print(f'Você ganhou {cores['amarelo']}{cont} vezes')
