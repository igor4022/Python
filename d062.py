print('''      RESOLVEDOR DE PA
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
n1 = int(input('Digite um número...'))
n2 = int(input('Digite mais um número...'))
nes = ''
rez = n1
cont = 1

cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',}

for cont in range(1, 10):
    rez += n2
    cont += 1

    print('{}{}{} =>'.format(cores['amarelo'], rez, cores['limpa']), end='')

while nes != 0:
    nes = int(input('Deseja digitar mais um número? Sé não dígite 0...'))
    cont = 1

    while cont <= 10:
        nes += n2
        cont += 1

        print('{}{}{} =>'.format(cores['azul'], nes, cores['limpa'] ), end='')


print('FIM')