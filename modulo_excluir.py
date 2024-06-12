def excluir_elemento(lista):
    armazenador=input("\nDigite o item a ser excluido\n")
    try:
        armazenador=lista.index(armazenador)
        del(lista[armazenador])
        print("Excluído!")
    except:
        print("Inexistente")
    return lista
