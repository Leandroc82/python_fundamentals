#-*-coding:utf-8-*-


# class Passaro():
#     #metodo construtor
#     def __init__(self):
#         self.asas = 2
#         self.penas = True
#         self.bico = True
#         self.patas = 2
#     #atributos
#     def voar(self):
#         if self.asas < 2:
#             self.cont = 0
#             print('passaro deficiente')
#         else:
#             self.cont = 1
#             print('voando...')
    
#     def pousar(self):
        
#         if self.cont == 0:
#             pass
#         else:
#             print('Pousando...')
    
#     def comer(self):
#         print('comendo...')

#     def dormir(self):
#         print('dormindo...')

# sabia = Passaro()
# sabia.voar()
# sabia.asas = 1
# print(sabia.asas)


# class Servidor():
#     def __init__(self, cpu, memoria, disco):
#         self.cpu = 2
#         self.memoria = 2048
#         self.disco = 500
#         #inserir
#     def inserirMemoria(self, mem):
#         self.memoria += mem
#     def inserirCPU(self, CPU):
#         self.cpu += CPU
#     def inserirDisco(self, disco):
#         self.disco += disco
#         #remove
#     def removeMemoria(self, mem):
#         self.memoria -= mem
#     def removeCPU(self, CPU):
#         self.cpu -= CPU
#     def removeDisco(self, disco):
#         self.disco -= disco

# ServidorWeb = Servidor('2 vcpu', '16BG', '50GB')
# ServidorWeb.inserirMemoria(1024)
# # ServidorWeb.inserirCPU(10)
# # ServidorWeb.inserirDisco(300)

# # ServidorWeb.removeMemoria(1024)
# # ServidorWeb.removeCPU(10)
# # ServidorWeb.removeDisco(300)


# # print(ServidorWeb.cpu)
# # print(ServidorWeb.memoria)
# # print(ServidorWeb.disco)


class Pai():
    def __init__(self):
        sobrenome = 'Pereira'
        profissao = 'Advogado'

    def trabalha(self)
        print('Advoga...')

class Filho(Pai):
    def __init__(self):
        print('Acessando a classe filho')

joao = Pai()
augusto = Filho()
print(augusto.sobrenome)0