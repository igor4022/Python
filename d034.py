res1 = float(input('Digite um número...'))
res2 = float(input('Digite mais um número...'))
res3 = float(input('Digite um último número...'))
cores = {'verde':'\033[32m',
         'vermelho':'\033[31m',}

if res1 < res2 + res3 and res2 < res1 + res3 and res3 < res1 + res2:
    print('Essas medidas {}formam um triangulo'.format(cores['verde']))
else:
    print('Essas medidas {}não formam um triangulo'.format(cores['vermelho']))