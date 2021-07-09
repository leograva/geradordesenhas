import random

#define tamanho da senha
tamanho = 15

#habilitando opções - (0 para desligado e 1 para ligado)
optmaiuscula = 1 #opção de letras maíusculas
optminuscula = 1 #opção de letras minúsculas
optnumeros = 1   #opção de números
optespeciais = 1 #opção de caracteres especiais

#mapa de caracteres
maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWYXZ'
minusculas = 'abcdefghijklmnopqrstuvwyxz'
numeros = '1234567890'
especiais = '@#$%&*'
dicionario = ""

#variavel de criação da senha
senha = ''

#validação das opções habilitadas e adição na string onde será armazenada o dicionário de caracteres
if optmaiuscula == 1:
    dicionario+=maiusculas
if optminuscula == 1:
    dicionario+=minusculas
if optnumeros == 1:
    dicionario+=numeros
if optespeciais == 1:
    dicionario+=especiais
    
#loop de repetição para 
for i in range(tamanho):
    numero = random.randint(1,(len(dicionario)-1))
    senha+=dicionario[numero]

#JOBSON
#LEO


#imprime senha gerada
print('Senha:',senha)
