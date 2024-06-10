import os
def iniciar_bd():
    lista_temporaria=[]
    try:
        manipulador_bd=open("database.txt","r+")
        for i in manipulador_bd:
            lista_temporaria.append(i.replace("\n",""))
        manipulador_bd.close()
        os.remove("database.txt")
    except:
        print("Primeira Inicializacao concluida!\n")
    return lista_temporaria

def encerrar_bd(lista):
    manipulador_bd=open("database.txt","a")
    for elemento in lista:
        manipulador_bd.write(elemento)
        manipulador_bd.write("\n")
    manipulador_bd.close()

def senhas():
    senhas_temp=[]
    try:
        manipulador_senhas=open("senhas.txt","r+")
        for i in manipulador_senhas:
            senhas_temp.append(i.replace("\n",""))
        manipulador_senhas.close()
        os.remove("senhas.txt")
    except:
        senhas_temp.append(input("Sem senhas cadastradas, por favor crie uma!\n"))
    return senhas_temp

def senhas_encerrar(lista):
    manipulador_senhas=open("senhas.txt","a")
    for elemento in lista:
        manipulador_senhas.write(elemento)
        manipulador_senhas.write("\n")
    manipulador_senhas.close()

def verificar_senha(lista):
    senha=input("Senha para acesso:\n")
    if senha in lista:
        return "ok"
    else:
        return "not"
    
        
