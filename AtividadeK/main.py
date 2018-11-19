from model.Cartao import Cartao
from model.Quadro import Quadro
from model.Lista import Lista
from model.Comentario import Comentario
from model.Etiqueta import Etiqueta
from db import db

def main():
    menu = """**********Trello**********
    \n1 - Criar Quadro
    \n0 - Sair
    \nOpcao: 
    """

    menu2 = """**********Trello**********
    \n1 - Criar Lista
    \n2 - Adicionar Cartao
    \n0 - Sair
    \nOpcao: 
    """

    menu3 = """**********Acoes do Cartao**********
    \n1 - Comentar
    \n2 - Arquivar
    \n3 - Alterar data de entrega
    \n0 - Sair
    \nOpcao: 
    """
    
    while True:
        opcao = int(input(menu))
        teste = None

        if opcao == 1:
            nome_quadro = input("Nome do quadro: ")
            quadro = Quadro(nome_quadro)

            while True:
                opcao = int(input(menu2))

                if opcao == 1:
                    nome_lista = input("Nome da lista: ")
                    quadro.adicionar_lista(nome_lista)

                elif opcao == 2:
                    listas = quadro.listas_quadro()
                    for lista in listas:
                        print("******Escolha uma lista do Quadro {}******\n{} - {}\n").format(quadro.get_titulo(), lista.get_id(), lista.get_titulo())
                    
                    opcao_lista = input("Opcao: ")
                    titulo_cartao = input("Titulo do cartao: ")

                    quadro.adicionar_cartao(titulo_cartao, opcao_lista)
                                                            
                    while True:
                        opcao1 = input(menu3)

                        def opcao_cartao():
                            print("******Escolha um Cartao da Lista******\n")
                            for cartao  in quadro.listar_cartaos(quadro.get_id()):
                                print("{} - {}\n".format(cartao.get_id(), cartao.get_titulo()))
                            
                            id_cartao = input("Opcao: ")
                            return id_cartao

                        if opcao1 == 1:
                            cartao = opcao_cartao()
                            comentario = input("Comentario: ")
                            quadro.comentar_cartao(teste, id_cartao, comentario)
                        
                        elif opcao1 == 3:
                            cartao = opcao_cartao()
                            data = input("Data: ")
                            quadro.alterar_data_entrega(cartao, data)

                        elif opcao1 == 0:
                            break

                elif opcao == 0:
                    break

        elif opcao == 0:
            break


if __name__ ==  "__main__":
    main()