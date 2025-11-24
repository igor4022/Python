n1 = int(input("Digite um valor..."))
n2 = int(input("Digite outro valor..."))
raz = n1
cont = 1

cores = {'limpa':'\033[m',
         'amarelo':'\033[1;33m',}

while cont <= 10:
    print('{}{}{} =>'.format(cores['amarelo'], raz, cores['limpa']), end='')
    raz += n2
    cont += 1
