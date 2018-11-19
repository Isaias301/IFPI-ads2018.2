from db import db
import random
from model.Lista import Lista
from model.Cartao import Cartao
from model.Comentario import Comentario


class Quadro:
    __id = None
    __titulo = None
    __particular = True


    def __init__(self, titulo):
        self.set_titulo = titulo
        self.salvar_quadro()


    def get_id(self):
        return self.id


    def get_titulo(self):
        return self.__titulo


    def get_particular(self):
        return self.particular


    def set_titulo(self, titulo):
        self.titulo = titulo


    def set_particular(self, particular):
        self.particular = particular


    def __set_id(self):
        self.id = random.randint(1,100)

    
    def adicionar_lista(self, nome):
        lista = Lista(nome)
        db["quadro_lista"].append({"quadro": self, "lista": lista})


    def salvar_quadro(self):
        self.__set_id()
        db["quadro"].append(self)


    
