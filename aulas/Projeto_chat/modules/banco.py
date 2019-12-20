# from pymongo import MongoClient, DESCENDING
# import time

# try:
#     client = MongoClient('192.168.200.139')
#     db =client['chat']
# except Exception as e:
#     print(f'ERRO {e}')
#     exit()

#     def cadastrar(nome, mensagem):
#         date = {
#             'nome' : nome,
#             'mesagem' : mensagem,
#             'horas' : time.strftime('%d-%m-%y %H:%M:%S')
#         }
#         db.chat.insert(date)

#     def select():
#         ultimo = [x for x in db.chat.find().sort("_id", DESCENDING)]
#         while True:
#             date = [x for x in db.chat.find().sort("_id", DESCENDING)]
#             if date != ultimo:
#                 ultimo = date              
#                 print('[{}] {}: {} \n'.format(date[0]['hora'],date[0]['nome'], date[0]['mensagem']))
#             time.sleep(2)

###############################################3

from pymongo import MongoClient, DESCENDING
import time

class BancoMongo():

    def __init__(self):
        try:
            client = MongoClient('localhost')
            self.db =client['chat']
        except Exception as e:
            print(f'ERRO: {e}')
            exit()

    def cadastrar(self, nome, mensagem):
        date = {
            'nome': nome,
            'mensagem': mensagem,
            'hora': time.strftime('%d-%m-%Y %H:%M:%S')
            }
        self.db.chat.insert(date)

    def select(self):
        ultimo = [x for x in self.db.chat.find().sort("_id", DESCENDING)]
        while True:
            date = [x for x in self.db.chat.find().sort("_id", DESCENDING)]
            if date != ultimo:
                ultimo = date
                print('[{}] {}: {} \n'.format(date[0]['hora'],date[0]['nome'], date[0]['mensagem']))
            time.sleep(1)

