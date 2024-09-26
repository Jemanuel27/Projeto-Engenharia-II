import tkinter as tk
from tkinter import messagebox

def adicionar_item(frame_conteudo, itens):
    tk.Label(frame_conteudo, text="Adicionar Item:").pack(pady=5)
    entrada_item = tk.Entry(frame_conteudo)
    entrada_item.pack(pady=5)

    def salvar_item():
        item = entrada_item.get()
        if item:
            itens.append(item)
            messagebox.showinfo("Sucesso", "Item adicionado com sucesso!")
            entrada_item.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Digite um item válido!")

    tk.Button(frame_conteudo, text="Salvar", command=salvar_item).pack(pady=5)
