from datetime import datetime, timedelta
import sqlite3
from tkinter import messagebox

def criar_tabela(conn):
    cursor = conn.cursor()
    
    # Criação da tabela, se não existir
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS compromissos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        data_hora TEXT NOT NULL
    )
    """)
    conn.commit()

# Função para verificar os compromissos próximos (nos próximos 5 minutos)
def verificar_compromissos(conn, root):
    # Obtém o horário atual
    agora = datetime.now()
    limite = agora + timedelta(minutes=5)  # Limite de 5 minutos para o lembrete

    cursor = conn.cursor()
    cursor.execute("SELECT id, descricao, data_hora FROM compromissos")
    compromissos = cursor.fetchall()

    for compromisso in compromissos:
        compromisso_id, descricao, data_hora = compromisso
        data_hora_obj = datetime.strptime(data_hora, '%Y-%m-%d %H:%M')  # Converte para objeto datetime

        # Se o compromisso está dentro do limite de 5 minutos
        if agora <= data_hora_obj <= limite:
            # Exibe uma mensagem de lembrete
            messagebox.showinfo("Lembrete", f"Você tem um compromisso: {descricao} às {data_hora}")
    
    # Após 1 minuto, verificar novamente (sem travar a interface)
    root.after(60000, verificar_compromissos, conn, root)  # A função é chamada novamente após 60 segundos (1 minuto)