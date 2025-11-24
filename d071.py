cores = {'amarelo': '\033[33m',
         'limpa': '\033[m',}

print('=-' * 20)
print('{}{:^30}{}'.format(cores['amarelo'], 'BANCO', cores['limpa']))
print('=-' * 20)
sacar = float(input(f'Digite o valor que deseja secar...'))
cedula = sacar
cinquenta = 50
cont = 0

while True:
 if cedula >= cinquenta:
    cedula -= cinquenta
    cont += 1

 else:
     print(f'Total de cedulas de {cores['amarelo']}R${cinquenta:.2f}{cores['limpa']}: {cores['amarelo']}{cont}{cores['limpa']}')
     if cinquenta == 50:
       cinquenta = 20

     elif cinquenta == 20:
       cinquenta = 10

     elif cinquenta == 10:
        cinquenta = 1
     cont = 0

     if cedula == 0:
      break
