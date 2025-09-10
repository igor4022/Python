nome = str(input('Digite seu nome completo...')).strip()

print('Seu nome em letras maieúsculas fica...{}'.format(nome.upper()))
print('Seu nome em leras minúsculas fica...{}'.format(len(nome.lower())))
print('Seu nome completo tem no total de...{} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem o total de...{} letras'.format(nome.find(' ')))