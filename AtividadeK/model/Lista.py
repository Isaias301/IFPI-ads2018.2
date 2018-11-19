from db import db
import random


class Lista:
    __id = None
    __titulo = None


    def __init__(self, titulo):
        self.set_titulo(titulo)
        self.salvar_lista()


    def get_id(self):
        return self.id


    def get_titulo(self):
        return self.titulo


    def set_titulo(self, titulo):
        self.titulo = titulo

    
    def __set_id(self):
        self.id = random.randint(1,100)


    def adicionar_cartao(self):
        pass


    def copiar_lista(self):
        pass


    def arquivar_todos_cartoes(self):
        pass


    def arquivar_lista(self):
        for lista in db["lista"]:
            if lista.id == self.get_id():
                db["lista"].remove(lista)
                return True
            else:
                return False

    
    def salvar_lista(self):
        self.__set_id()
        db["lista"].append(self)