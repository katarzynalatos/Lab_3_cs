from Player import Player
from Board import Board
import logging

class GomokuStarter:
    def __init__(self):
        self.size=-1
        self._name=""
        self.sign=0

    def Start(self,Client):
        Client.send(str.encode("\nG O M O K U\nWhat is your name?"))
        d = Client.recv(1024)
        self._name = d.decode()
        logging.info("Player typed name.")
        while len(self._name) == 0:
            Client.send(str.encode("Incorrect data.Type your name again\n"))
            logging.info("Player typed incorrect data.")
            d=Client.recv(1024)
            self._name=d.decode()
            logging.info("Player typed name.")
        try:
            Client.send(str.encode('{} what board size do you prefer? Choose 3,4,5,6,7,8,9 or 10'.format(self._name)))
            logging.info("Player typed board size.")
            d = Client.recv(1024)
            self.size=int(d.decode())
        except ValueError:
            self.size=0
        while self.size <=2 or self.size >= 11:
            try:
                Client.send(str.encode('This size is incorrect.\n{} what board size do you prefer? Choose 3,4,5,6,7,8,9 or 10'.format(self._name)))
                logging.info("Player typed incorrect data.")
                d = Client.recv(1024)
                self.size = int(d.decode())
                logging.info("Player typed board size.")
            except ValueError:
                self.size=0
        try:
            Client.send(str.encode('Would you like "O" or "X"? "O" type 1, "X" type -1'))
            d = Client.recv(1024)
            self.sign = int(d.decode())
            logging.info("Player typed board sign.")
        except ValueError:
            self.sign=0
        while self.sign!=-1 and self.sign!=1:
            try:
                Client.send(str.encode('This is incorrect number. Choose again. "O" type 1, "X" type -1'))
                logging.info("Player typed incorrect data.")
                d = Client.recv(1024)
                self.sign = int(d.decode())
                logging.info("Player typed sign.")
            except ValueError:
                self.sign=0
    def return_player(self):
        player = Player(self._name, self.sign,1) # player nr=1
        return player
    def return_board(self):
        board = Board(self.size)
        return board



