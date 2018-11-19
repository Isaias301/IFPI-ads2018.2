from db import db
import random


class Comentario:
    __id = None
    __comentario = None


    def __init__(self, comentario):
        self.set_comentario(comentario)
        self.salvar_comentario()


    def get_id(self):
        return self.id


    def get_comentario(self):
        return self.comentario


    def __set_id(self):
        self.id = random.randint(1,100)


    def set_comentario(self, comentario):
        self.comentario = comentario


    def salvar_comentario(self):
        self.__set_id()
        db["comentario"].append(self)


    def editar(self, comentario):
        self.set_comentario(comentario)


    def excluir(self):
        for comentario in db["comentario"]:
            if comentario.id == self.get_id():
                db["comentario"].remove(comentario)
                return True
            else:
                return False