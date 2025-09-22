saldo = float(input('Qual é seu salário...'))
res1 = saldo * 1.10
res2 = saldo * 1.15
cores = {'verde':'\033[32m',
         'amarelo':'\033[33m',
         'branco':'\033[m',}

if saldo <= 1250:
    print('O seu almento de {}15%{} foi de {}R${:.2f}'.format(cores['amarelo'],cores['branco'], cores['verde'], res2))
else:
    print('O seu almento é de {}10%{} foi de {}R${:.2f}'.format(cores['amarelo'],cores['branco'], cores['verde'], res2))
