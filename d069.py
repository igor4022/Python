cont = 0
cont2 = 0
cont3 = 0

cores = {'limpa': '\033[m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'vermelho': '\033[31m',
         'roxo': '\033[35m',
         'titulo': '\033[4;33;40m',}

print(f'''         {cores['titulo']}CADASTRO DE PESSOAS{cores['limpa']}
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')

while True:
    print(f'''--------------------------------------
             {cores['amarelo']}CADASTRE-SE{cores['limpa']}
--------------------------------------''')
    idade = int(input('Qual a sua idade?...'))
    sexo = str(input(f'Qual o seu sexo {cores['azul']}M{cores['limpa']}/{cores['vermelho']}F{cores['limpa']}...')).strip().upper()[0]
    print('---------------------------------------')
    res = str(input(f'Quer continuar {cores['verde']}S{cores['limpa']}/{cores['vermelho']}N{cores['limpa']}...')).strip().upper()[0]

    if idade >= 18:
        cont += 1

    if sexo == 'M':
        cont2 += 1

    if sexo == 'F' and idade <= 20:
        cont3 += 1

    if res not in 'Ss':
        print('FIM')
        break


print(f'Tem {cores['roxo']}{cont}{cores['limpa']} pessoas que são maiores de 18 anos que foram {cores['amarelo']}cadastrados{cores['limpa']}.')
print(f'Tem {cores['azul']}{cont2}{cores['limpa']} homens que foram {cores['amarelo']}cadastrados{cores['limpa']}.')
print(f'Tem {cores['vermelho']}{cont3}{cores['limpa']} mulheres com menos de 20  que foi {cores['amarelo']}cadastradas')
