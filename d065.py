num = 0
res = 'S'
cont = 0
soma = 0
maior = 0
menor = 0

cores = {'amarelo': '\033[33m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'limpa': '\033[m',
         'azul': '\033[34m',}

print('''-----> Digite números e o computador descobrira a média, o menor e o maior número que você digitou <------
----------------------------------------------------------------------------------------------------------''')

while res in 'Ss':
    num = int(input('Digite um número...'))
    res = str(input('Quer continuar? [{}S{}/{}N{}]...'.format(cores['verde'], cores['limpa'], cores['vermelho'], cores['limpa']))).upper().strip()[0]
    cont += 1
    soma += num / cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print('Você digitou {}{}{} números, a média dos seus valores é {}{:.1f}{}, além disso o maior número digitado é o {}{}{} e o menor número digitado é o {}{}'.format(cores['azul'], cont, cores['limpa'],cores['amarelo'], soma + 0.5, cores['limpa'], cores['verde'], maior, cores['limpa'], cores['vermelho'], menor))