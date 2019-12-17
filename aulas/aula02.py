#-*-coding:utf-8-*-

##revisao
import os
# Entrada e saida de dados

#Entrada: input()
#Saida: Print()

# nome = input('digite seu nome')

# print(f'o nome digitado foi {nome}')


# num = int(input('digite numero: '))

# print(f'o nome digitado foi {num} numero x 15: {(num * 15)} ')

#repeticao while e for

# numeros = [1, 2, 3, 4, 5, 6]
# multiplicados = []

# for numero in numeros:
#     multiplicados.append(numero * 15)
#     #print(multiplicados)
# print(multiplicados)

# ou

# #numeros = [1, 2, 3, 4, 5, 6]
# multiplicados = [i*15 for i in range (1 , 7)]

# print(multiplicados)




# erros e exceçoes 

# while True:
#     try:
#         x = int(input('Digite o primeiro numero: '))
#         y = inp(input('digite o segundo numero: '))
#     except ValueError as e:
#         print('Tipo invalido')


# if else elif


# print('Bem vindo ao Banco T!')
# print('Escolha uma oção abaixo:')
# print('Digite 1 para saque')
# print('Digite 2 para deposito')
# print('Digite 9 para sair')
# opcao = int(input('>>> '))

# while True:
#     opcao = int(input('>>> '))
#     if opcao == 1:
#         print('Saque selecionado!')
#         break
#     elif opcao == 2:
#         print('Deposito selecionado!')
#         break
#     elif opcao == 9:
#         print('Obrigado, volte sempre!')
#         break
#     else:
#         print('Opção Inválida')
#         continue

# print('Digite seu sexo: ')
# print('M - para masculino')
# print('F - para feminino')

# if user.lower == m:
#     print("Usuario de sexo masculino")
#     break
# elif s_user == f:
#     print('Usuario de sexo feminino')
#     break
# else:
#     print('Entrada invalida')
#     continue

# usuarios = ['ana', 'bruno', 'caio','camila','joao']


# try:
#     login = input('digite seu login: ')
#     if login not in usuarios:
#         raise  NameError('usuario nao cadastrado')
#     else:
#         print(f'Bem vindo {login}')

# except NameError as n:
#     print (n)


#manipulacao de arquivo

with open('arquivo.txt', 'a') as p:
    p.write('teste04')
    p.close()