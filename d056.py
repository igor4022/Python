somaidade = 0
mediaidade = 0
maioridade = 0
nomevelho = ''
mulher = 0

for cont in range(1, 5):
    print('-----{}° PESSOA-----'.format(cont))
    nome = input('Digite seu nome...')
    idade = input('Digite sua idade...')
    sexo = str(input('Digite seu sexo (M/F)...')).strip()
    somaidade += idade
    if cont == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1

mediaidade = somaidade / 4
print('A media de idade das pessos digitadas é {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridade, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))