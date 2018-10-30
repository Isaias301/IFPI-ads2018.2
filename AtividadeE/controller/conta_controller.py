from model.conta_model import Conta


def abrir_conta(titula, cpf, rg):
    try:
        conta = Conta(titula, cpf, rg)
        retorno = {"mensagem": "Conta aberta com sucesso"}
        return retorno
    except:
        retorno = {"mensagem": "Erro ao abrir conta"}
        return retorno   
