class View():
    largura = 0
    altura = 0


    def altura(self, altura):
        if altura <= 100 or altura >= 0:
            self.altura = altura
    

    def largura(self, largura):
        if largura <= 100 or largura >= 0:
            self.largura = largura