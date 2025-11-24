val = int(input('Digite um valor...'))
cont = 0

cores = {'amarelo':'\033[33m',
          }

while cont <= val:
    cont += 1
    print('{}{}'.format(cores['amarelo'], cont))
    