from random import randint
import logging


class Play:
    def __init__(self,board, player0, player1):
        self.board=board
        self.player0=player0
        self.player1=player1

    def play(self, Client, player_nr,correct_step):
        if player_nr==0:
            position_x = randint(1, self.board.size)
            position_y = randint(1, self.board.size)
            while not self.board.is_empty(position_x, position_y):
                position_x = randint(1, self.board.size)
                position_y = randint(1, self.board.size)
            self.board.set_position(position_x, position_y, self.player0.sign,Client,self.player0)
            return True
        else:
            try:
                board = self.board.write_board()
                Client.send(str.encode(board + "It's your turn now!\nGive row (X) position of your choice"))
                d = Client.recv(1024)
                position_x = int(d.decode())
            except ValueError:
                position_x=0
            while position_x < 1 or position_x > self.board.size:
                try:
                    Client.send(str.encode('Incorrect position number. Give row (X) position of your choice from [1,{}]'.format(self.board.size)))
                    logging.info("Player typed incorrect position.")
                    d = Client.recv(1024)
                    position_x = int(d.decode())
                    logging.info("Player typed position x.")
                except ValueError:
                    position_x=0
            try:
                Client.send(str.encode('Give column (Y) position of your choice'))
                d = Client.recv(1024)
                position_y = int(d.decode())
            except ValueError:
                position_y = 0
            while position_y < 1 or position_y > self.board.size:
                try:
                    Client.send(str.encode(
                        'Incorrect position number. Give column (Y) position of your choice from [1,{}]'.format(self.board.size)))
                    logging.info("Player typed incorrect position.")
                    d = Client.recv(1024)
                    position_y = int(d.decode())
                    logging.info("Player typed position y.")
                except ValueError:
                    position_y=0

            if self.board.set_position(position_x, position_y, self.player1.sign, Client, self.player0):
                return True
            else:
                return False
