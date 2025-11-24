abaixo = 0
cont = 0
soma = 0
barato = ''
menor = 0

cores = {'limpa': '\033[m',
         'titulo': '\033[4;33;40m',
         'amarelo': '\033[33m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'azul': '\033[34m',}

print(f'''       {cores['titulo']}MAQUINA de CONTABILISAÇÃO de COMPRAS{cores['limpa']}
=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=''')

while True:
    print(f'''---------------------------------------
                {cores['amarelo']}PRODUTO{cores['limpa']}                      
---------------------------------------''')
    nome = str(input('Digite seu nome do produto...'))
    valor = float(input('Digite o valor do produto...'))
    res = str(input(f'''---------------------------------------
{cores['azul']}Quer colocar mais um produto{cores['limpa']} {cores['verde']}S{cores['limpa']}/{cores['vermelho']}N{cores['limpa']}...''')).strip().upper()[0]
    soma += valor
    cont += 1

    if valor <= 1000:
        abaixo += 1

    if cont == 1:
        menor = valor
        barato = nome
    else:
        if valor < menor:
            menor = valor
            barato = nome

    if res not in 'Ss':
        print(f'{cores['vermelho']}FIM{cores['limpa']}')
        break

print(f'O valor de todos os produtos somados é {cores['amarelo']}R${soma:.2f}{cores['limpa']}')
print(f'Teve {cores['amarelo']}{abaixo}{cores['limpa']} produtos que foram a baixo de {cores['amarelo']}R$1000{cores['limpa']}')
print(f'O produto mais barato digitado foi {cores['amarelo']}{barato}{cores['limpa']} e o valor foi {cores['amarelo']}R${menor:.2f}{cores['limpa']}')
