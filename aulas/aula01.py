#!/usr/bin/python3

## Identação

# nome = input('Digite seu nome: ')

# if nome == str: # : após condicionais
#     print('nome é uma string') # identação de 4 espaços

# else: # : após condicionais
#     print('nome nã é uma string') # identação de 4 espaços


## Entrada e saída de dados

# nome = input('Digite seu nome: ')

# print(nome)

# numero = float(input('Digite um número: '))

# print(type(numero))

## métodos de string

# texto = 'isso é uma string'

# print(texto.upper())
# print(texto.capitalize())
# print(texto.count('a'))
# print(texto.isnumeric())
# print(texto.split(' '))
# print('.'.join(texto))
# print(texto.replace('i', 'o'))


#dada a lista abaixo:

lista = ['Corinthians', [1, 2, 3, 4, 5] ,
         'Palmeiras', 'São Paulo', 
        [10, 11, 12, 13, 14],'Flamengo', 'Vasco']



# # print 3, 13, Vasco
# print(lista[1][2], lista[-3][-2] lista[-1])

# # print 5, São Paulo, 14
# print(lista[1][-1], lista[3][-2] lista[-1])

# # mude o valor de 4 para 40
# # mude o valor de 14 para 150

dados = {

    'cidades': {
        'saopaulo': {
            'nome': 'São Paulo',
            'municipios': 645,
            'população': 12.18
        },
        'riodejaneiro': {
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'população': 6.32
        },
        'minasgerais': {
            'nome': 'Minas Gerais',
            'municipios': 31,
            'população': 20.87

        }
    }
}


# imprima a quantiddade de municipios de minas
#print(dados['cidades']['minasgerais']['municipios'])
# imprima a quantidade de municipios do rio
#print(dados['cidades'])

# imprima o nome e população de são paulo em milhoes


# ['rafaela','luis', 'joao', 'ana', 'paulo', 'fernando', 'marilia', 'tarcisio', 'carlos', 'manuel']


# faça um for que imprima o nome de cada pessoa da lista e com a mensagem 'bem-vindo {}'
nomes = ['rafaela','luis', 'joao', 'ana', 'paulo', 'fernando', 'marilia', 'tarcisio', 'carlos', 'manuel']

for nome in nomes:
    print(f'bem-vindo {nome}')



