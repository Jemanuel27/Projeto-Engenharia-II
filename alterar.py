import tkinter as tk
from tkinter import messagebox

def alterar_item(frame, itens):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Nome do Item para Alterar:").pack(pady=5)
    nome_entry = tk.Entry(frame)
    nome_entry.pack(pady=5)

    tk.Label(frame, text="Nova Quantidade:").pack(pady=5)
    quantidade_entry = tk.Entry(frame)
    quantidade_entry.pack(pady=5)

    def alterar():
        nome = nome_entry.get()
        nova_quantidade = int(quantidade_entry.get())
        for item in itens:
            if item['nome'] == nome:
                item['quantidade'] = nova_quantidade
                messagebox.showinfo("Sucesso", "Item alterado com sucesso!")
                return
        messagebox.showerror("Erro", "Item não encontrado.")

    tk.Button(frame, text="Alterar", command=alterar).pack(pady=10)