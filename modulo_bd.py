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