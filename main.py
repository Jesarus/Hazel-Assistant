import tkinter as tk
import sqlite3
from utils import *
from funcionalidades import *

# Abrir a conexão globalmente
conn = sqlite3.connect('compromissos.db')

# Chama a função para garantir que a tabela existirá
criar_tabela(conn)

# Função para adicionar compromisso
def adicionar_compromisso():
    adicionar_compromisso_interface(conn, root)

# Função para mostrar compromissos
def mostrar_compromissos():
    mostrar_compromissos_interface(conn, root)

# Função para fechar o programa e a conexão
def fechar_programa():
    conn.close()  # Fechar a conexão com o banco de dados
    root.quit()  # Fechar a aplicação

# Configuração da interface principal
root = tk.Tk()
root.title("Assistente de Compromissos")
root.geometry("400x400")

# Iniciar a verificação de compromissos
verificar_compromissos(conn, root)

# Botões para interagir com a IA
adicionar_btn = tk.Button(root, text="Adicionar Compromisso", command=adicionar_compromisso)
adicionar_btn.pack(pady=20)

mostrar_btn = tk.Button(root, text="Mostrar Compromissos", command=mostrar_compromissos)
mostrar_btn.pack(pady=10)

fechar_btn = tk.Button(root, text="Fechar", command=fechar_programa)
fechar_btn.pack(pady=10)

root.mainloop()