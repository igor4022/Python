from time import sleep

cores = {'azul':'\033[34m'}

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('{}BOOM!!!'.format(cores['azul']))