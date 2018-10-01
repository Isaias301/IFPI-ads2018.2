class Conta:
    # atributos
    nome = None
    cpf = None
    tipo_conta = None
    saldo = 0


    # metodos
    def get_nome(self):
        return self.nome

    
    def get_cpf(self):
        return self.cpf


    def get_tipo_conta(self):
        return self.tipo_conta


    def set_nome(self, nome):
        self.nome = nome


    def set_cpf(self, cpf):
        self.cpf = cpf


    def set_tipo_conta(self, tipo_conta):
        self.tipo_conta = tipo_conta


    def tranferencia(self, agencia, conta, valor, agendamento):
        mensagem = ""
        if self.cpf and self.saldo > 0 and self.saldo > valor:
            mensagem = "{} transferido para {}/{} com sucesso.".format(valor,agencia, conta)
        else:
            mensagem = "Saldo insuficiente"


    def deposito(self, valor):
        self.saldo = valor
        mensagem = "Valor depositado com sucesso."
        return mensagem

    
    def saque(self, valor):
        mensagem = ""
        if self.saldo > valor:
            mensagem = "Contando cédulas..."
        else:
            mensagem = "Saldo insuficiente"


    def saldo(self):
        return self.saldo