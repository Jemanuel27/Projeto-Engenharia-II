def alterar_elemento(lista):
    armazenador=input("\nDigite a tarefa a ser alterada\n")
    try:
        armazenador=lista.index(armazenador)
        lista[armazenador]=input("Digite a tarefa com a alteracao\n")
        print("Tarefa alterada!")
    except:
        print("Tarefa inexistente")
    return lista