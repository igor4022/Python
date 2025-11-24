frase = str(input('Digeite um número...')).upper().strip()
palavra = frase.split()
junto = ' '.join(palavra)
inverso  = ''

cores = {'azul': '\033[34m',
         'amarelo': '\033[33m',
         'limpa': '\033[m', }

for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print('A palavra digitada foi {}{}{} e au contrario fica assim {}{}{}'.format(cores['amarelo'], junto, cores['limpa'], cores['amarelo'], inverso, cores['limpa']))

if inverso == junto:
    print('A sua frase é um é um {}PALÍNDROMO!!!'.format(cores['azul']))
else:
    print('A sua frase ficou  {}MUITO BOA!!!'.format(cores['azul']))