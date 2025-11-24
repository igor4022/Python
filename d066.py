res = cont = 0
val = soma = 0

cores = {'verde': '\033[32m',
         'limpa': '\033[m',}

while True:
    val = int(input('Digite um número [Só vai parrar até sair o número 999]...'))
    cont += 1

    if val == 999:
        break

    soma += val
    res = cont

print(f'Foram digitados {cores['verde']}{res}{cores['limpa']} e soma dos valores é {cores['verde']}{soma}')

