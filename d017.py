import math

num1 = float(input('Escolha um numero para o cateto oposto...'))
num2 = float(input('Escolha outro um numero para o cateto adjacente...'))

hip = (math.sqrt(num1**2 + num2**2))

cos = hip / num1
cose = hip / num2
tang = cos / cose

print('O seu COS é {}, o seu COSENO é {} e sua TANGENTE é {}'.format(cos, cose, tang))