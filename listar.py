import tkinter as tk

def listar_itens(frame_conteudo, itens):
    if itens:
        tk.Label(frame_conteudo, text="Itens:").pack(pady=5)
        for item in itens:
            tk.Label(frame_conteudo, text=item).pack()
    else:
        tk.Label(frame_conteudo, text="Nenhum item encontrado.").pack(pady=5)
