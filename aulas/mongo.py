import pymongo

from pymongo import MongoClient

cliente = MongoClient('localhost')
db.cliente['dexterops']

def inserir_dados():
    try:
        db.fila.insert({"_id":10, "empresa": "dexterops",
                         "produtos": [
                             "produto01": "camiseta batman preta",
                             "produto02": "camiseta lanterna verde",
                             "produto03": "caneca star wars",
                             "produto04": "camiseta python"
                         ]
        })
    except Exception as e:
    print(f'Erro: {e}')
if __name__ == "__main__"
    inserir_dados()


