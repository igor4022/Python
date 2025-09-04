val = float(input('Escreva o valor para descobrir o preço com 5% de desconto...'))
des = 5 / 100 * val
res = val - des

print('O valor da compra com o desconto de 5% é de R${}'.format(res))