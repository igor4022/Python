frase = 'Curso em Vídeo Python'

print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[1::2])

print("""Exemplos de CONDIÇÕES:
3:13
:13
13:
1:15:2
1::2""")

print(frase.upper().count('o'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('Python'))
print(frase.lower().find('vídeo'))
print(frase.split())