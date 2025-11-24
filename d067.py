tab = 0
vez = 0
cont = 0

cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'azul': '\033[34m',}

while True:
    val = int(input('Digite um valor para saber sua tabuada...'))

    if val < 0:
     break

    for tab in range(0, 10):
      cont += 1
      vez = val * cont

      print(f'{cores['amarelo']}{val}{cores['limpa']} X {cores['azul']}{cont}{cores['limpa']} = {cores['vermelho']}{vez}{cores['limpa']}')