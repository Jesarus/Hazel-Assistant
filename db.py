import sqlite3

# Função para criar conexão com o banco
def criar_conexao():
    conn = sqlite3.connect("compromissos.db")
    return conn

# Função para criar a tabela no banco
def criar_tabela():
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS compromissos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        data_hora TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Função para adicionar compromisso
def adicionar_compromisso(descricao, data_hora):
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO compromissos (descricao, data_hora) VALUES (?, ?)", (descricao, data_hora))
    conn.commit()
    conn.close()

# Função para recuperar compromissos
def recuperar_compromissos():
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM compromissos")
    compromissos = cursor.fetchall()
    conn.close()
    return compromissos

# Função para editar compromisso
def editar_compromisso(compromisso_id, nova_descricao, nova_datahora):
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("UPDATE compromissos SET descricao=?, data_hora=? WHERE id=?", (nova_descricao, nova_datahora, compromisso_id))
    conn.commit()
    conn.close()

# Função para remover compromisso
def remover_compromisso(compromisso_id):
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM compromissos WHERE id=?", (compromisso_id,))
    conn.commit()
    conn.close()