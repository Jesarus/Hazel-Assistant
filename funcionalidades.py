import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Função para adicionar compromisso
def adicionar_compromisso_interface(conn, root):
    # Criando uma nova janela
    janela_adicionar = tk.Toplevel(root)
    janela_adicionar.title("Adicionar Compromisso")
    janela_adicionar.geometry("400x300")

    # Rótulos e campos para inserir a descrição e data/hora
    tk.Label(janela_adicionar, text="Descrição:").pack(pady=5)
    descricao_entry = tk.Entry(janela_adicionar, width=40)
    descricao_entry.pack(pady=5)

    # Obter data e hora atual para preencher automaticamente o campo de data/hora
    datahora_atual = datetime.now().strftime('%Y-%m-%d %H:%M')  # Exemplo de formato: 2025-03-15 14:30

    tk.Label(janela_adicionar, text="Data e Hora (YYYY-MM-DD HH:MM):").pack(pady=5)
    datahora_entry = tk.Entry(janela_adicionar, width=40)
    datahora_entry.insert(0, datahora_atual)  # Preenche com a data e hora atual
    datahora_entry.pack(pady=5)

    # Função para adicionar o compromisso no banco de dados
    def adicionar():
        descricao = descricao_entry.get()
        datahora = datahora_entry.get()
        if descricao and datahora:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO compromissos (descricao, data_hora) VALUES (?, ?)", (descricao, datahora))
            conn.commit()
            messagebox.showinfo("Sucesso", "Compromisso adicionado com sucesso!")
            janela_adicionar.destroy()  # Fecha a janela após adicionar
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    # Botão para adicionar compromisso
    tk.Button(janela_adicionar, text="Adicionar", command=adicionar).pack(pady=10)

# Função para mostrar os compromissos
def mostrar_compromissos_interface(conn, root):
    nova_janela = tk.Toplevel(root)
    nova_janela.title("Compromissos")
    nova_janela.geometry("400x400")

    cursor = conn.cursor()
    cursor.execute("SELECT id, descricao, data_hora FROM compromissos")
    compromissos = cursor.fetchall()

    def excluir_compromisso(compromisso_id):
        cursor.execute("DELETE FROM compromissos WHERE id = ?", (compromisso_id,))
        conn.commit()
        mostrar_compromissos_interface(conn, root)
        nova_janela.destroy()

    def editar_compromisso(compromisso_id, descricao, data_hora):
        editar_janela = tk.Toplevel(nova_janela)
        editar_janela.title("Editar Compromisso")
        editar_janela.geometry("400x200")

        tk.Label(editar_janela, text="Descrição:").pack(pady=5)
        descricao_entry = tk.Entry(editar_janela, width=40)
        descricao_entry.insert(0, descricao)
        descricao_entry.pack(pady=5)

        tk.Label(editar_janela, text="Data e Hora (YYYY-MM-DD HH:MM):").pack(pady=5)
        datahora_entry = tk.Entry(editar_janela, width=40)
        datahora_entry.insert(0, data_hora)
        datahora_entry.pack(pady=5)

        def salvar_edicao():
            nova_descricao = descricao_entry.get()
            nova_datahora = datahora_entry.get()
            cursor.execute("UPDATE compromissos SET descricao = ?, data_hora = ? WHERE id = ?", 
                           (nova_descricao, nova_datahora, compromisso_id))
            conn.commit()
            editar_janela.destroy()
            mostrar_compromissos_interface(conn, root)
            nova_janela.destroy()

        tk.Button(editar_janela, text="Salvar", command=salvar_edicao).pack(pady=10)

    for compromisso in compromissos:
        compromisso_id, descricao, data_hora = compromisso
        
        compromisso_frame = tk.Frame(nova_janela)
        compromisso_frame.pack(pady=10)

        tk.Label(compromisso_frame, text=f"{descricao} - {data_hora}", font=("Arial", 12)).pack(side="left", padx=10)
        
        editar_btn = tk.Button(compromisso_frame, text="Editar", 
                               command=lambda c_id=compromisso_id, desc=descricao, dh=data_hora: editar_compromisso(c_id, desc, dh))
        editar_btn.pack(side="left", padx=5)
        
        excluir_btn = tk.Button(compromisso_frame, text="Excluir", 
                                command=lambda c_id=compromisso_id: excluir_compromisso(c_id))
        excluir_btn.pack(side="left", padx=5)