class Arcondicionado():
    """
        Classe Ar-condicionado
    """

    ligado = False
    marca = None
    cor = None
    btus = None
    modelo = None
    temp = None
    velocidade = None
    swing = None


    def __init__(self, marca, cor, btus, modelo, swing):
        self.ligado = False
        self.marca = marca
        self.cor = cor
        self.btus = btus
        self.modelo = modelo
        self.swing = False


    def set_ligar(self):
        if self.ligado:
            mensagem = "O aparelho ja está ligado"
            return mensagem
        else:
            self.ligado = True
    

    def set_desligar(self):
        if self.ligado:
            self.ligado = False
        else:
            mensagem = "O aparelho ja está desligado"
            return mensagem
            

    def set_aumentar_velocidade(self, valor):
        if self.velocidade < 3:
            try:
                self.velocidade += valor 
            except ValueError as erro:
                return erro
        else:
            mensagem = "Velocidade maxima e 3"
            return mensagem


    def set_diminuir_velocidade(self, valor):
        if self.velocidade > 0:
            try:
                self.velocidade += valor 
            except ValueError as erro:
                return erro
        else:
            mensagem = "Velocidade ja está no 0"
            return mensagem


    def get_marca(self):
        return self.marca


    def get_cor(self):
        return self.cor
    

    def get_estado_atual(self):
        return self.ligado


    def get_arcondicionado(self):
        return self.ligado, self.marca, self.cor, self.btus, self.modelo, self.temp, self.velocidade, self.swing


a = Arcondicionado("gree", "branco", 900, "UJ-09")
