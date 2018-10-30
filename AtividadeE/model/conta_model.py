class Conta:
    __saldo = 0
    __titular = None
    __cpf = None
    __rg = None
    __numero = None
    __agencia = None
    __data_abertura = None
    __data_cancelamento_conta = None
    __opcao_credito = None
    __usuario = None
    __senha = None


    def __init__(self, titula, cpf, rg):
        self.__set_tiular = titula
        self.__set_cpf = cpf
        self.__set_rg = rg


    def __get_saldo(self):
        return self.__saldo


    def __get_tiular(self):
        return self.__titular


    def __get_cpf(self):
        return self.__cpf


    def __get_rg(self):
        return self.__rg


    def __get_numero(self):
        return self.__numero

    
    def __get_agencia(self):
        return self.__agencia


    def __get_data_abertura(self):
        return self.__data_abertura

    
    def __get_data_cancelamento_conta(self):
        return self.__data_cancelamento_conta


    def __get_opcao_credito(self):
        return self.__opcao_credito


    def __get_usuario(self):
        return self.__usuario


    def __get_senha(self):
        return self.__senha


    def __set_saldo(self, saldo):
        self.__saldo = saldo


    def __set_tiular(self, titular):
        self.__titular = titular


    def __set_cpf(self, cpf):
        self.__cpf = cpf


    def __set_rg(self, rg):
        self.__rg = rg


    def __set_numero(self, numero):
        self.__numero = numero

    
    def __set_agencia(self, agencia):
        self.__agencia = agencia


    def __set_data_abertura(self, data_abertura):
        self.__data_abertura = data_abertura

    
    def __set_data_cancelamento_conta(self, data_cancelamento_conta):
        self.__data_cancelamento_conta


    def __set_opcao_credito(self, opcao_credito):
        self.__opcao_credito = opcao_credito


    def __set_usuario(self, usuario):
        self.__usuario = usuario


    def __set_senha(self, senha):
        self.__senha = senha


    def depositar(self, **kwargs):
        pass


    def sacar(self, **kwargs):
        pass


    def transferencia(self, **kwargs):
        pass


    def nova_conta(self, **kwargs):
        pass


    def extrato(self, **kwargs):
        pass


    def fechar_conta(self, **kwargs):
        pass
        
    
    
