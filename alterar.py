import tkinter as tk
from tkinter import messagebox

def alterar_item(frame, itens):
    for widget in frame.winfo_children():
        widget.destroy()

    label_style = {"font": ("Arial", 12), "anchor": 'w'}
    
    tk.Label(frame, text="Nome do Item para Alterar:", **label_style).pack(pady=10, padx=20, anchor='w')
    nome_entry = tk.Entry(frame, font=("Arial", 12), bg="#f0f0f0")
    nome_entry.pack(pady=5, padx=20, fill='x')

    tk.Label(frame, text="Nova Quantidade:", **label_style).pack(pady=10, padx=20, anchor='w')
    quantidade_entry = tk.Entry(frame, font=("Arial", 12), bg="#f0f0f0")
    quantidade_entry.pack(pady=5, padx=20, fill='x')

    def alterar():
        nome = nome_entry.get()
        try:
            quantidade = int(quantidade_entry.get())
            for item in itens:
                if item['nome'] == nome:
                    item['quantidade'] = quantidade
                    messagebox.showinfo("Sucesso", "Item alterado com sucesso!")
                    return
            messagebox.showerror("Erro", "Item não encontrado.")
        except ValueError:
            messagebox.showerror("Erro", "A quantidade deve ser um número válido.")

    # Estilo do botão (deve ser definido antes da criação do botão)
    button_style = {
        "font": ("Arial", 12, "bold"),
        "bg": "#063970",  # Cor de fundo verde
        "fg": "white",    # Cor da fonte
        "width": 20,
        "height": 2,      
        "bd": 0,
        "relief": "flat"    
    }

    # Botão de Alterar com estilo
    tk.Button(frame, text="Alterar", command=alterar, **button_style).pack(pady=35, padx=0)

    # Forçar o frame a se reorganizar
    frame.update_idletasks()

# Testando a função alterar_item
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    
    # Lista de itens (exemplo)
    itens = [{"nome": "Item1", "quantidade": 10}, {"nome": "Item2", "quantidade": 5}]

    # Frame principal
    frame_conteudo = tk.Frame(root, bg='white')
    frame_conteudo.pack(fill='both', expand=True)

    # Inicialmente chama a função para alterar itens
    alterar_item(frame_conteudo, itens)

    root.mainloop()
