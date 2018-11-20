from db import db
import random


class Cartao:
    __id = None
    __titulo = None
    __data_entrega = None


    def __init__(self, titulo):
        self.set_titulo(titulo)


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
        self.__set_id()
        db["cartao"].append(self)
        self.log("criando cartao")


    def comentario(self, comentario):
        pass


    def log(self, log):
        db["log_cartao"].append({"id_cartao": self.get_id, "log": log})