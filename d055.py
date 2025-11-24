maior = 0
menor = 0

for conut in range(1,6):
    peso = int(input('Digite o {} peso...'.format(conut)))

    if  conut == 1:
        maior = conut
        menor = conut
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}kg'.format(maior))
print('E o menor peso é {}kg'.format(menor))
