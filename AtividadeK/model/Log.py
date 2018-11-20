import random
from db import db


class Log:
    __id = None
    __log = None


    def __init__(self, log):
        self.__set_log(log)


    def get_id(self):
        return self.id


    def get_log(self):
        return self.log


    def __set_id(self):
        self.id = random.randint(1,100)


    def __set_log(self, log):
        self.log = log


    def salvar(self):
        db["log"].append(self.get_log())
