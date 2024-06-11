import modulo_adicionar, modulo_listar, modulo_alterar, modulo_excluir, modulo_bd, sys
try:
    indicador_funcao=1
    database=modulo_bd.iniciar_bd()
    senhas=modulo_bd.senhas()
    if(modulo_bd.verificar_senha(senhas)=="ok"):
        print("Bem vindo a BorderSystems - Projeto Dahl")
        while(indicador_funcao!=0):
            indicador_funcao=int(input("\nDigite 1 para tarefas\nDigite 2 para senhas\nDigite 0 para sair\n"))
            if(indicador_funcao==1):
                while(indicador_funcao!=5):
                    indicador_funcao=int(input("\nDigite 1 para adicionar um item\nDigite 2 para listar itens cadastrados\nDigite 3 para editar algum item\nDigite 4 para excluir um item\nDigite 5 para voltar\n"))        
                    if(indicador_funcao==1):
                        database=modulo_adicionar.adicionar_elemento(database)
                    elif(indicador_funcao==2):
                        modulo_listar.listar_elementos(database)
                    elif(indicador_funcao==3):
                        database=modulo_alterar.alterar_elemento(database)
                    elif(indicador_funcao==4):
                        database=modulo_excluir.excluir_elemento(database)
                    elif(indicador_funcao!=1 and indicador_funcao!=2 and indicador_funcao!=3 and indicador_funcao!=4 and indicador_funcao!=5):
                        print("Digite uma operacao valida!")
            elif(indicador_funcao==2):
                while(indicador_funcao!=5):
                    indicador_funcao=int(input("\nDigite 1 para adicionar uma senha\nDigite 2 para listar senhas cadastradas\nDigite 3 para editar alguma senha\nDigite 4 para excluir uma senha\nDigite 5 para voltar\n"))
                    if(indicador_funcao==1):
                        senhas=modulo_adicionar.adicionar_elemento(senhas)
                    elif(indicador_funcao==2):
                        modulo_listar.listar_elementos(senhas)
                    elif(indicador_funcao==3):
                        senhas=modulo_alterar.alterar_elemento(senhas)
                    elif(indicador_funcao==4):
                        senhas=modulo_excluir.excluir_elemento(senhas)
                    elif(indicador_funcao!=1 and indicador_funcao!=2 and indicador_funcao!=3 and indicador_funcao!=4 and indicador_funcao!=5):
                        print("Digite uma operacao valida!")
            elif(indicador_funcao!=1 and indicador_funcao!=2 and indicador_funcao!=0):
                print("Digite uma operacao valida!")
            else:
                print("Até a próxima!")
    else:
        print("Senha inválida, acesso negado")
    modulo_bd.encerrar_bd(database)
    modulo_bd.senhas_encerrar(senhas)
except:
    print("Operação inválida, encerrando sistema!")
    modulo_bd.encerrar_bd(database)
    modulo_bd.senhas_encerrar(senhas)
    
