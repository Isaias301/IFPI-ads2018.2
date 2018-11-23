from db import db
import random
from model.Lista import Lista
from model.Cartao import Cartao
from model.Log import Log
from model.Etiqueta import Etiqueta
from model.Comentario import Comentario


class Quadro:
    __id = None
    __titulo = None
    __particular = True


    def __init__(self, titulo):
        self.__set_id()
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
        lista.salvar_lista()
        db["quadro_lista"].append({"quadro": self, "lista": lista})
        

    def salvar_quadro(self):
        db["quadro"].append(self)
        

    def listas_quadro(self):
        listas = []
        for quadro_lista in db["quadro_lista"]:
            if quadro_lista["quadro"].get_id() == self.get_id():
                listas.append(quadro_lista["lista"])
        return listas


    def listar_cartaos(self, quadro):
        cartoes = []
        for cartao in db["quadro_lista_cartao"]:
            if cartao["quadro"].get_id() == quadro:
                cartoes.append(cartao["cartao"])
        return cartoes


    def adicionar_cartao(self, titulo, lista):
        cartao = Cartao(titulo)
        cartao.salvar_cartao()

        lista_quadro = None
        for lista_encontrada in db["quadro_lista"]:
            if lista_encontrada["lista"].get_id() == lista:
                lista_quadro = lista_encontrada["lista"]
        db["quadro_lista_cartao"].append({"quadro": self, "lista": lista_quadro, "cartao": cartao})
        data = {"mensagem": "Cartao adicionado a lista {}".format(self.get_titulo(), lista_quadro.get_titulo())}
        log = Log(data)
        log.salvar()
    

    def comentar_cartao(self, lista, cartao, texto_comentario):
        comentario = Comentario(texto_comentario)
        db["quadro_lista_cartao_comentario"].append({"quadro": self, "lista": lista, "cartao": cartao, "comentario": comentario})
        data = {"mensagem": "Cartao {} comentado".format(cartao)}
        log = Log(data)
        log.salvar()


    def alterar_data_entrega(self, id_cartao, data):
        for cartao in db["cartao"]:
            if cartao.get_id() == cartao:
                cartao.alterar_data_entrega(data)
        data = {"mensagem": "Data do cartao {} alterada.".format(id_cartao)}
        log = Log(data)
        log.salvar()

    
    def adicionar_etiqueta(self, cor, cartao):
        etiqueta = Etiqueta(cor)
        etiqueta.salvar()
        db["quadro_lista_cartao_etiqueta"].append({"quadro": self, "cartao": cartao, "etiqueta": etiqueta})
        data = {"mensagem": "Etiqueta adicionada ao cartao {}.".format(cartao)}
        log = Log(data)
        log.salvar()


    def mover_cartao(self, lista, cartao):
        # print(lista)
        # print(cartao)
        # for i in db["quadro_lista_cartao_comentario"]:
        #     if i["cartao"].get_id() == cartao:
        #         db["quadro_lista_cartao_comentario"].remove()
        pass
        

    def arquivar_cartao(self, cartao):
        a = None
        for cartao in db["cartao"]:
            if cartao.get_id() == cartao:
                cartao.set_arquivar()
                a = cartao
        print(a)
    

    def log_cartao(self, cartao):
        return db["log"] 

