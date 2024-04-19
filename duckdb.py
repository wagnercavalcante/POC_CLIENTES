import duckdb

# Criar uma conexão com o DuckDB (usando uma conexão em memória)
# conn = duckdb.connect(database=':memory:')
conne = duckdb.connect(database='caminho/para/arquivo.duckdb')


# Executar uma consulta SQL
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER, name VARCHAR)")
cursor.execute("INSERT INTO users VALUES (1, 'Alice')")
cursor.execute("INSERT INTO users VALUES (2, 'Bob')")

# Executar uma consulta de seleção
cursor.execute("SELECT * FROM users")
# Recuperar os resultados
results = cursor.fetchall()
# Exibir os resultados
for row in results:
    print(row)

# Fechar a conexão
conn.close()
