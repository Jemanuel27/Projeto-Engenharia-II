def alterar_elemento(lista):
    armazenador=input("\nDigite o item a ser alterado\n")
    try:
        armazenador=lista.index(armazenador)
        lista[armazenador]=input("Digite o item com a alteração\n")
        print("Alterado!")
    except:
        print("Inexistente")
    return lista
