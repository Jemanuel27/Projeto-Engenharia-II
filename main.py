import tkinter as tk
from tkinter import messagebox
import os

# Importar as funções dos módulos separados
from adicionar import adicionar_item
from listar import listar_itens
from alterar import alterar_item
from remover import remover_item

# Lista para armazenar os itens (simulação de banco de dados)
itens = []

# Definindo o tamanho padrão para todas as janelas
tamanho_padrao = "1280x720"  # Largura x Altura
redimensionavel = (False, False)  # Define se pode redimensionar (largura, altura)

# Função para centralizar uma janela
def centralizar_janela(janela, largura, altura):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura // 2)
    y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

# Função para atualizar o conteúdo da área central dinamicamente
def atualizar_conteudo(funcao):
    for widget in frame_conteudo.winfo_children():
        widget.destroy()
    funcao(frame_conteudo, itens)

# Função para exibir a tela CRUD após login
def mostrar_tela_crud():
    global frame_conteudo

    tela_crud = tk.Toplevel()
    tela_crud.title("CRUD")
    tela_crud.geometry(tamanho_padrao)
    tela_crud.resizable(*redimensionavel)
    centralizar_janela(tela_crud, 1280, 720)  
    
    # Frame para o menu
    frame_menu = tk.Frame(tela_crud, bg="lightgray", width=540, height=10)
    frame_menu.pack(side="top", fill="x", pady=55)  # Preenche horizontalmente

    # Estilização dos botões (remover bordas)
    estilo_botao = {"font": ("Verdana", 12), "bg": "#063970", "fg": "white", "width": 25, "height": 2, "bd": 0, "relief": "flat"}

    # Criar botões de menu
    tk.Button(frame_menu, text="Adicionar", command=lambda: atualizar_conteudo(adicionar_item), **estilo_botao).pack(side="left", padx=35, pady=10, ipady=5)
    tk.Button(frame_menu, text="Listar", command=lambda: atualizar_conteudo(listar_itens), **estilo_botao).pack(side="left", padx=35, pady=10, ipady=5)
    tk.Button(frame_menu, text="Alterar", command=lambda: atualizar_conteudo(alterar_item), **estilo_botao).pack(side="left", padx=35, pady=10, ipady=5)
    tk.Button(frame_menu, text="Remover", command=lambda: atualizar_conteudo(remover_item), **estilo_botao).pack(side="left", padx=35, pady=10, ipady=5)

    # Frame de conteúdo
    frame_conteudo = tk.Frame(tela_crud, bg="white")
    frame_conteudo.pack(side="bottom", fill="both", padx=20, pady=10)

# Função para verificar login
def verificar_login():
    senha_digitada = entrada_senha_login.get()
    if os.path.exists("senha.txt"):
        with open("senha.txt", "r") as arquivo:
            senha_salva = arquivo.read()
        if senha_digitada == senha_salva:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            tela_login.withdraw()
            mostrar_tela_crud()
        else:
            messagebox.showerror("Erro", "Senha incorreta!")
    else:
        messagebox.showerror("Erro", "Nenhuma senha criada! Por favor, crie uma senha primeiro.")

# Função para criar a senha
def criar_senha():
    senha = entrada_senha.get()
    confirmar_senha = entrada_confirmar_senha.get()
    if senha == confirmar_senha:
        with open("senha.txt", "w") as arquivo:
            arquivo.write(senha)
        messagebox.showinfo("Sucesso", "Senha criada com sucesso!")
        tela_criar_senha.destroy()
        mostrar_tela_login()
    else:
        messagebox.showerror("Erro", "As senhas não coincidem!")

# Função para mostrar a tela de criação de senha
def mostrar_tela_criar_senha():
    global tela_criar_senha, entrada_senha, entrada_confirmar_senha
    tela_criar_senha = tk.Toplevel(tela_login)
    tela_criar_senha.title("Criar Senha")
    tela_criar_senha.geometry(tamanho_padrao)
    tela_criar_senha.resizable(*redimensionavel)
    centralizar_janela(tela_criar_senha, 600, 400)  # Centralizar janela de criação de senha

    # Estilização de labels e entradas
    estilo_label = {"font": ("Arial", 12), "bg": "lightblue"}
    estilo_entrada = {"font": ("Arial", 12), "width": 25, "show": "*"}

    tk.Label(tela_criar_senha, text="Digite a nova senha:", **estilo_label).pack(pady=5)
    entrada_senha = tk.Entry(tela_criar_senha, **estilo_entrada)
    entrada_senha.pack(pady=5)
    tk.Label(tela_criar_senha, text="Confirme a senha:", **estilo_label).pack(pady=5)
    entrada_confirmar_senha = tk.Entry(tela_criar_senha, **estilo_entrada)
    entrada_confirmar_senha.pack(pady=5)
    tk.Button(tela_criar_senha, text="Criar Senha", command=criar_senha, font=("Arial", 12), bg="#063970", fg="white", bd=0, relief="flat").pack(pady=20)

# Função para mostrar a tela de login
def mostrar_tela_login():
    global tela_login, entrada_senha_login
    tela_login = tk.Tk()
    tela_login.title("Login")
    tela_login.geometry(tamanho_padrao)
    tela_login.resizable(*redimensionavel)
    centralizar_janela(tela_login, 600, 400)  # Centralizar janela de login

    # Estilização de labels e botões de login
    estilo_label = {"font": ("Arial", 12)}
    estilo_entrada = {"font": ("Arial", 12), "width": 25}
    estilo_botao = {"font": ("Verdana", 12), "bg": "#063970", "fg": "white", "width": 15, "height": 2, "bd": 0, "relief": "flat"}

    tk.Label(tela_login, text="Digite sua Senha:", **estilo_label).pack(pady=10)
    entrada_senha_login = tk.Entry(tela_login, **estilo_entrada, show="*")
    entrada_senha_login.pack(pady=5)
    tk.Button(tela_login, text="Login", command=verificar_login, **estilo_botao).pack(pady=10)
    tk.Button(tela_login, text="Criar Nova Senha", command=mostrar_tela_criar_senha, **estilo_botao).pack(pady=5)
    tela_login.mainloop()

# Iniciar o programa mostrando a tela de login
mostrar_tela_login()
