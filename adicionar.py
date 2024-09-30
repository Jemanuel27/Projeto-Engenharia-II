import tkinter as tk
from tkinter import messagebox

def adicionar_item(frame, itens):
    # Limpar os widgets existentes no frame antes de adicionar novos
    for widget in frame.winfo_children():
        widget.destroy()

    # Estilo personalizado para labels
    label_style = {"font": ("Arial", 12), "anchor": 'w'}

    # Adicionar espaçamento nas labels e campos de entrada com estilos
    tk.Label(frame, text="Nome do Item:", **label_style).pack(pady=10, padx=20, anchor='w')
    nome_entry = tk.Entry(frame, font=("Arial", 12), bg="#f0f0f0", bd=2, relief="solid")
    nome_entry.pack(pady=5, padx=20, fill='x')

    tk.Label(frame, text="Quantidade:", **label_style).pack(pady=10, padx=20, anchor='w')
    quantidade_entry = tk.Entry(frame, font=("Arial", 12), bg="#f0f0f0", bd=2, relief="solid")
    quantidade_entry.pack(pady=5, padx=20, fill='x')

    # Função de adicionar o item à lista
    def adicionar():
        nome = nome_entry.get()
        try:
            quantidade = int(quantidade_entry.get())
            if nome and quantidade > 0:
                itens.append({'nome': nome, 'quantidade': quantidade})
                messagebox.showinfo("Sucesso", "Item adicionado com sucesso!")
                nome_entry.delete(0, tk.END)  # Limpar campos após adição
                quantidade_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", "Por favor, preencha um nome e uma quantidade válida.")
        except ValueError:
            messagebox.showerror("Erro", "A quantidade deve ser um número válido.")

    # Estilo do botão
    button_style = {
        "font": ("Arial", 12, "bold"),
        "bg": "#4CAF50",  # Cor de fundo verde
        "fg": "white",    # Cor da fonte
        "activebackground": "#45a049",  # Cor ao clicar
        "bd": 0,          # Borda
        "relief": "flat"  # Estilo de relevo
    }

    # Botão de Adicionar com estilo
    tk.Button(frame, text="Adicionar", command=adicionar, **button_style).pack(pady=20, padx=20)

    # Adicionar padding ao frame para espaçamento interno
    frame.pack_propagate(False)
    frame.pack(padx=40, pady=40, fill="both", expand=True)

# Testando a interface simples
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    
    # Lista de itens
    itens = []

    # Frame principal para o conteúdo
    frame_conteudo = tk.Frame(root, bg='white')
    frame_conteudo.pack(fill='both', expand=True)

    # Chama a função para adicionar itens ao iniciar a janela
    adicionar_item(frame_conteudo, itens)

    root.mainloop()
