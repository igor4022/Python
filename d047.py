from time import sleep

cores = {'azul':'\033[34m'}

for cont in range(50, 0, -2):
    print(cont)
    sleep(1)
print('{}FIM!!!'.format(cores['azul']))