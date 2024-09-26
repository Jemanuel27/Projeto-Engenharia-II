import tkinter as tk
from tkinter import messagebox

def remover_item(frame_conteudo, itens):
    tk.Label(frame_conteudo, text="Remover Item:").pack(pady=5)
    entrada_item_remover = tk.Entry(frame_conteudo)
    entrada_item_remover.pack(pady=5)

    def salvar_remocao():
        item = entrada_item_remover.get()
        if item in itens:
            itens.remove(item)
            messagebox.showinfo("Sucesso", "Item removido com sucesso!")
        else:
            messagebox.showerror("Erro", "Item não encontrado!")

    tk.Button(frame_conteudo, text="Remover", command=salvar_remocao).pack(pady=5)
