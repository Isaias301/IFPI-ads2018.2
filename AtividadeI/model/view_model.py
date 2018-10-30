class View():
    largura = 0
    altura = 0


    def altura(self, altura):
        """
            Adiciona uma altura e verifica se está dentro dos requisitos
        """
        if altura <= 100 or altura >= 0:
            self.altura = altura
    

    def largura(self, largura):
        """
            Adiciona uma largura e verifica se está dentro dos requisitos
        """
        if largura <= 100 or largura >= 0:
            self.largura = largura