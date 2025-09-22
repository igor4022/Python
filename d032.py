num1 = int(input('Digite um número...'))
num2 = int(input('Digite outro número...'))
num3 = int(input('Digite um último último...'))
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
cores = {'verde':'\033[32m',
         'vermelho':'\033[31m',
         'branco':'\033[0m',}

print('O maior número é o {}{}{} e o menor é o {}{}'.format(cores['verde'], maior, cores['branco'], cores['vermelho'], menor))