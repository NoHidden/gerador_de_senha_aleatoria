#gerador de senha aleatoria
import os
import random

letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '!@#$%&*/\?'

x = letras_minusculas + letras_maiusculas + numeros +simbolos

tamanho_da_senha = int(input('Digite o tamanho da senha desejada: '))
senha = ''.join(random.sample(x, tamanho_da_senha))

senha_de = input('De onde é essa senha: ')

with open('senhas.txt', 'a', encoding='utf-8') as arquivo:
    for i in senha:
        arquivo.write(senha_de+': '+senha+os.linesep)
        print(f'Sua nova senha aleatoria é: {senha}')
        break
