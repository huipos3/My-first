import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

tamanho = int(input('Digite o tamanho da senha:'))

senha = ' '

for i in range(tamanho):
    caracter = random.choice(caracteres)
    senha += caracter

print('Sua senha é: ', senha)
