res1 = float(input('Digite um número...'))
res2 = float(input('Digite mais um número...'))
res3 = float(input('Digite um último número...'))

cores = { 'verde':'\033[32m',
          'amarelo':'\033[33m',
          'azul':'\033[34m',}

if res1 == res2 == res3:
    print('{}Equilátero'.format(cores['verde']))
elif res1 != res2 != res3:
    print('{}Escaleno'.format(cores['amarelo']))
elif res1 != res2 or res2 != res3:
    print('{}Isósceles'.format(cores['azul']))