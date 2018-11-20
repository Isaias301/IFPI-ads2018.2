from db import db
import random
from model.Log import Log


class Etiqueta:
    __id = None
    __nome = None
    __cor = None


    def __init__(self, cor):
        self.__set_id()
        self.set_cor(cor)


    def get_id(self):
        return self.id


    def get_nome(self):
        return self.nome


    def get_cor(self):
        return self.cor


    def __set_id(self):
        self.id = random.randint(1,100)


    def set_nome(self, nome):
        self.nome = nome


    def set_cor(self, cor):
        self.cor = cor


    def salvar(self):
        self.__set_id()
        db["etiqueta"] = self
        data = {"mensagem": "Etiqueta {} adicionada ao cartao.".format(self.get_cor())}
        log = Log(data)
        log.salvar()


    def excluir(self):
        for etiqueta in db["etiqueta"]:
            if etiqueta.id == self.get_id():
                db["etiqueta"].remove(etiqueta)
                return True
            else:
                return False