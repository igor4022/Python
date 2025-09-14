n = str(input('Digite seu nome completo...')).strip()
nome = n.split()

print('O seu prímeiro nome é {}'.format(nome[0]))
print('O seu úlimo nome é {}'.format(nome[len(nome)-1]))