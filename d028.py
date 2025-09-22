km = int(input('Quantos Km voce percorreu...'))
mul =  km * 7
multa = mul - km
cores = {'vermelha':'\033[0;31m',
         'verde':'\033[0;32m',}

if km >= 70:
    print('Voce foi multado!!!')
    print('A sua multa é de {}R${:.2f}'.format(cores['vermelha'], multa))
else:
    print('{}Tá de boa então...'.format(cores['verde']))