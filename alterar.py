import tkinter as tk
from tkinter import messagebox

def alterar_item(frame_conteudo, itens):
    tk.Label(frame_conteudo, text="Alterar Item:").pack(pady=5)
    tk.Label(frame_conteudo, text="Item Antigo:").pack(pady=5)
    entrada_item_antigo = tk.Entry(frame_conteudo)
    entrada_item_antigo.pack(pady=5)

    tk.Label(frame_conteudo, text="Item Novo:").pack(pady=5)
    entrada_item_novo = tk.Entry(frame_conteudo)
    entrada_item_novo.pack(pady=5)

    def salvar_alteracao():
        item_antigo = entrada_item_antigo.get()
        item_novo = entrada_item_novo.get()
        if item_antigo in itens:
            index = itens.index(item_antigo)
            itens[index] = item_novo
            messagebox.showinfo("Sucesso", "Item alterado com sucesso!")
        else:
            messagebox.showerror("Erro", "Item não encontrado!")

    tk.Button(frame_conteudo, text="Alterar", command=salvar_alteracao).pack(pady=5)
