class Computador:
    # atributos
    tela = None
    ligar = False
    teclado = False
    mouse = False
    drive_cd = False
    

    # metodos
    def get_tela(self):
        return self.tela


    def get_ligar(self):
        return self.ligar


    def get_teclado(self):
        return self.teclado


    def get_mouse(self):
        return self.mouse


    def get_drive_cd(self):
        return self.drive_cd


    def set_tela(self, tela):
        self.tela = tela


    def set_ligar(self, ligar):
        self.ligar = ligar


    def set_teclado(self, teclado):
        self.teclado = teclado


    def set_mouse(self, mouse):
        self.mouse = mouse


    def set_drive_cd(self, drive_cd):
        self.drive_cd = drive_cd


    def abri_programa(self, programa):
        mensagem = ""
        if self.ligar:
            mensagem = "Iniciando programa {}".format(programa)
        else:
            mensagem = "Por favor ligue o computador primeiro"
        return mensagem

    
    def fechar_programa(self, programa):
        mensagem = ""
        if self.ligar:
            mensagem = "Fechando programa {}".format(programa)
        else:
            mensagem = "Por favor ligue o computador primeiro"
        return mensagem

    
    def ligar_teclado(self):
        mensagem = ""
        if self.ligar:
            mensagem = "Teclado ativado com sucesso"
        else:
            mensagem = "Por favor ligue o computador primeiro"
        return mensagem


    def desligar_teclado(self):
        mensagem = ""
        if self.ligar:
            mensagem = "Teclado desativado com sucesso"
        else:
            mensagem = "Por favor ligue o computador primeiro"
        return mensagem


    def abrir_drive_cd(self):
        mensagem = ""
        if self.ligar:
            mensagem = "Drive de cd aberto"
        else:
            mensagem = "Por favor ligue o computador primeiro"
        return mensagem


    def fechar_drive_cd(self):
        mensagem = ""
        if self.ligar:
            mensagem = "Drive de cd fechado"
        else:
            mensagem = "Por favor ligue o computador primeiro"
        return mensagem

    
    def ligar_tela(self):
        mensagem = ""
        if self.ligar:
            mensagem = "Tela ativa com sucesso"
        else:
            mensagem = "Por favor ligue o computador primeiro"
        return mensagem


    def desligar_tela(self):
        mensagem = ""
        if self.ligar:
            mensagem = "Tela desativada com sucesso"
        else:
            mensagem = "Por favor ligue o computador primeiro"
        return mensagem