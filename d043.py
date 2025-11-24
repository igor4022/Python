val = float(input('Digite sua forma de pagamento...'))

din = val - ((10/100) * val)
cart = val - ((5/100) * val)
mas = val * (20/100)
jus = val + mas

paga = float(input('''Digite sua forma de pagamento:
                       *Digite 1 para dinhero / cheque
                       *Digite 2 para cartão
                       *Digite 3 para 2x no cartão
                       *digite 4 para 3x
                       Digite aqui...'''))

cores = {'verde': '\033[32m',
         'branco': '\033[m'}

if paga == 1 :
    print('Você ganhou {}10%{} de desconto na sua compra, você vai pagar no total {}R${}'.format(cores['verde'], cores['branco'], cores['verde'], din))
elif paga == 2 :
    print('Você ganhou {}5%{} de desconto na sua compra, você vai pagar no total {}R${}'.format(cores['verde'], cores['branco'], cores['verde'], cart))
elif paga == 3 :
    print('O valor da sua compra foi de {}R${}'.format(cores['verde'], val))
elif paga == 4 :
    print('O valor de juros a ser pago é {}R${}{} e você vai pagar no total {}R${}'.format(cores['verde'], mas, cores['branco'], cores['verde'], jus))