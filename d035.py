casa = float(input('Qual o valor da casa?...'))
salario = float(input('Qual o seu salario?...'))
anos = float(input('Em quantos anos você prentende pagar?...'))

tempo = anos * 12
resultado = casa / tempo

cores = {'verde':'\033[32m',
         'vermelho':'\033[31m',}

if resultado >= salario * 0.30:
    input('Em felismente não é possível efetuar o calculo, pois seu valor de investimento utrapassa {}30%{} do seu salário'.format(cores['vermelho'], cores['vermelho']))
else:
    (input('Você vai ter que que pagar {}{}{} parcelas e o valor das parcelas é de {}R${:.1f}'.format(cores['verde'], tempo, cores['verde'], cores['verde'], resultado)))