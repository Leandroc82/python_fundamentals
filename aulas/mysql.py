import MySQLdb

try:
    con = MySQLdb.connect(host="localhost", user="admin", passwd="4linux", db="projetos")

    cur = con.cursor()

    cur.execute("insert into clientes(nome, endereco) values ('Carlos', 'Madureira')")

    con.commit()
    print('Registro criado com sucesso')
except Exception as e:
    print(f'Erro: {e}')
    print('Fazendo rollback')
    con.rollback

finally:
    print('Finalizando conexao com banco de dados')
    cur.close()
    con.close()