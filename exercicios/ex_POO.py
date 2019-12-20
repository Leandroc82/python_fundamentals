# criar uma classe automovel, com atributos:
#                             motor
#                             marca
#                             ano
#                             preco


# e com os metodos que retornam o valor de: 
#                             motor
#                             marca
#                             ano
#                             preco


# class Automovel():
#     def __init__(self, motor, marca, ano, preco):
#         self.marca = marca
#         self.motor = motor
#         self.ano = ano
#         self.preco = preco

#     def get_motor:
#         print(self.motor)
#     def get_marca:
#         print(self.marca)
#     def get_ano:
#         print(self.ano)
#     def get_preco:
#         print(self.preco)


#     # def marcaAuto(self, marca)
#     #     self.marca = marca

#     # def motorAuto(self, motor)
#     #     self moto = motor

#     # def anoAuto(self, ano)
# 0    #     self ano = ano

#     # def precoAuto(self, preco)
#     #     self preco = preco

#####################################################

# Faça uma classe de uma conta bancaria que tera os seguintes 
# atributos:
#             Nome do banco  Oldbak    
#             Número do banco    99
#             Número da agencia   
#             número da conta
#             nome do cliente
#             saldo


# métodos:
#         Sacar
#         Depositar
#         Extrato


# Menu

# 1 - para saque
# 2 - deposito
# 3 - extrato


# Extrato

# Nome do Banco
# ====================
# Clinte: tal
# Conta: tal Ag: ta
#  Saldo


 ###########################3

class Oldbak():
    def __init__(self, cl, cc, ag, sld=0, nome_banco='Oldbank', num_banco=99):
        self.client = cl
        self.conta = cc
        self.agencia = ag
        self.saldo = sld
        self.banco = banco
        self.n_banco = num_banco
    
    def deposito(self, valor):
        print(f'Saldo atual: '{self.saldo})
        deposito = float(input('Valor a ser depositado'))
        return self.saldo += deposito
    
