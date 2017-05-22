import logging


class Player:
    def __init__(self, name="Computer", sign=0, nr=0):
        logging.info("Player no "+str(nr)+" had sign: " +str(sign)+".")
        #player nr =1
        #computer nr=0
        self._name = name
        self.sign=sign
        #value -1 means X
        #value 1 means O
        self.nr=nr

