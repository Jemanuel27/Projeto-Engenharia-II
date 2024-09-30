import tkinter as tk

def listar_itens(frame, itens):
    for widget in frame.winfo_children():
        widget.destroy()

    if not itens:
        tk.Label(frame, text="Nenhum item cadastrado").pack(pady=10)
    else:
        for item in itens:
            tk.Label(frame, text=f"Nome: {item['nome']} - Quantidade: {item['quantidade']}").pack(pady=5)
