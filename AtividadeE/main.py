from controller.conta_controller import *

def main():
    menu = """**********Teste**********
    \n1 - Abrir conta
    \nOpcao: 
    """
         
    while True:
        opcao = int(input(menu))

        if opcao == 1:
            titula = input("Nome: ")
            cpf = input("CPF: ")
            rg = input("RG: ")
            conta = abrir_conta(titula, cpf, rg)
            print(conta["mensagem"])
        elif opcao == 0:
            break


if __name__ ==  "__main__":
    main()