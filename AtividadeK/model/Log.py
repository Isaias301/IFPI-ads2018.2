import random


class Log:
    __id = None
    __log = None


    def __init__(self):
        pass


    def get_id(self):
        return self.id


    def get_log(self):
        return self.log


    def __set_id(self):
        self.id = random.randint(1,100)