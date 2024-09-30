import tkinter as tk
from tkinter import messagebox

def remover_item(frame, itens):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Nome do Item para Remover:").pack(pady=5)
    nome_entry = tk.Entry(frame)
    nome_entry.pack(pady=5)

    def remover():
        nome = nome_entry.get()
        for item in itens:
            if item['nome'] == nome:
                itens.remove(item)
                messagebox.showinfo("Sucesso", "Item removido com sucesso!")
                return
        messagebox.showerror("Erro", "Item não encontrado.")

    tk.Button(frame, text="Remover", command=remover).pack(pady=10)
