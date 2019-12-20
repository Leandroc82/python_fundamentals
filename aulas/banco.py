import psycopg2

try:
    con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")
    cur = con.cursor()

    cur.execute("insert into scripts(nome, conteudo) values ('script.teste', 'conexao postgres')")

    con.commit()
    print('Registro criado com sucesso')

except Exception as e:
    print(f'ERRO: {(e)}')
    print('Fazendo rollback')
    con.rollback()
finally:
    print('Finalizando conexao com banco')
    cur.close()
    con.close()