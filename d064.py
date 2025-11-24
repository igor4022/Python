num = 0
cont = 0
res = 0

while num != 999:
     num =int(input('Digite um valor 999 para parrar...'))
     cont += 1
     res += num

print('Foram dígitados {} números e os números somados var dar o resultado será {}'.format(cont - 1, res - 999 ))
