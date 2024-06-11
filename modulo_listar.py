def listar_elementos(lista):
    if(lista!=[]):
        print("\nLista")
        for contador,elemento in enumerate(lista):
            print(contador+1,":",elemento)
    else:
        print("\nVazio!")
