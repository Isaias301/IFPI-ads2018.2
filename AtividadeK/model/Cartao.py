from db import db
import random
from model.Log import Log
from model.Comentario import Comentario


class Cartao:
    __id = None
    __titulo = None
    __data_entrega = None
    __arquivar = False


    def __init__(self, titulo):
        self.__set_id()
        self.set_titulo(titulo)


    def get_arquivar(self):
        return self.arquivar


    def get_data_entrega(self):
        return self.data_entrega


    def get_id(self):
        return self.id


    def get_titulo(self):
        return self.titulo


    def set_titulo(self, titulo):
        self.titulo = titulo


    def __set_id(self):
        self.id = random.randint(1,100)


    def set_data_entrega(self, data_entrega):
        self.data_entrega = data_entrega


    def set_arquivar(self):
        self.arquivar = True
        

    def arquivar(self):
        for cartao in db["cartao"]:
            if cartao.id == self.get_id():
                db["cartao"].remove(cartao)
                return True
            else:
                return False

    
    def alterar_data_entrega(self, data_enrtega):
        self.set_data_entrega(data_enrtega)


    def mover(self):
        pass

    
    def salvar_cartao(self):
        data = {"mensagem": "Cartao {} criado".format(self.get_titulo())}
        log = Log(data)
        log.salvar()