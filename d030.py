km = int(input('Quantos Km voce percorreu...'))
preso =  km * 0.50 #Preço de uma viagem padrão.
premas = km * 0.45 #Preço de viagem mais longa.
cores = {'vermelha':'\033[0;31m',
         'verde':'\033[0;32m'}

if km <= 200:
    print('O valor da passagem é de {}R${:.2f}'.format(cores['verde'], preso))
else:
    print('O valor da passagem é de  {}R${:.2f}'.format(cores['verde'], premas))