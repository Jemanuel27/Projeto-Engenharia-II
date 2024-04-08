import modulo_adicionar, modulo_listar, modulo_alterar, modulo_excluir, modulo_bd
indicador_funcao=5
database=modulo_bd.iniciar_bd()
print("Bem vindo a crissystems - To do List")
while(indicador_funcao!=0):
    print("\nDigite 1 para adicionar uma tarefa\nDigite 2 para listar as tarefas\nDigite 3 para editar alguma tarefa\nDigite 4 para excluir uma tarefa\nDigite 0 para sair")
    indicador_funcao=int(input())
    if(indicador_funcao==0):
        print("Até a próxima!")
    elif(indicador_funcao==1):
        database=modulo_adicionar.adicionar_elemento(database)
    elif(indicador_funcao==2):
        modulo_listar.listar_elementos(database)
    elif(indicador_funcao==3):
        database=modulo_alterar.alterar_elemento(database)
    elif(indicador_funcao==4):
        database=modulo_excluir.excluir_elemento(database)
    else:
        print("Digite uma operacao valida!")
modulo_bd.encerrar_bd(database)
