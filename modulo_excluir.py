def excluir_elemento(lista):
    armazenador=input("\nDigite a tarefa a ser excluida\n")
    try:
        armazenador=lista.index(armazenador)
        del(lista[armazenador])
        print("Tarefa excluida!")
    except:
        print("Tarefa inexistente")
    return lista