class Celular:
    # atributos
    tela = None
    ligar = False


    # metodos
    def get_tela(self):
        return self.tela


    def get_ligar(self):
        return self.ligar


    def set_tela(self, tela):
        self.tela = tela


    def set_ligar(self, ligar):
        self.ligar = ligar

    
    def fazer_ligacao(self, numero):
        mensagem = ""
        if self.ligar:
            mensagem = "Ligando para {}".format(numero)
        else:
            mensagem = "Celular desligado"

    
    def instalar_aplicativo(self, nome):
        mensagem = ""
        if self.ligar:
            mensagem = "Instalando aplicativo {}".format(nome)
        else:
            mensagem = "Celular desligado"


    def enviar_sms(self, numero, mensagem):
        mensagem = ""
        if self.ligar:
            mensagem = "Enviando mensagem para {}".format(numero)
        else:
            mensagem = "Celular desligado"


    def ouvir_musica(self, musica):
        mensagem = ""
        if self.ligar:
            mensagem = "Tocando musica {}".format(musica)
        else:
            mensagem = "Celular desligado"
