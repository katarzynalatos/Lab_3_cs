from random import randint

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
            self.board.set_position(position_x, position_y, self.player0.sign)
            return True
        else:
            try:
                board = self.board.write_board(Client)
                if correct_step==True:
                    Client.send(str.encode(board + 'Give row (X) position of your choice'))
                else:
                    Client.send(str.encode(board+"You have chosen not empty position. Choose another one\n" + 'Give row (X) position of your choice'))
                d = Client.recv(1024)
                position_x = int(d.decode())
            except ValueError:
                position_x=0
            while position_x < 1 or position_x > self.board.size:
                try:
                    Client.send(str.encode('Incorrect position number. Give row (X) position of your choice from [1,{}]'.format(self.board.size)))
                    d = Client.recv(1024)
                    position_x = int(d.decode())
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
                        'Incorrect position number. Give column (Y) position of your choice from [0,{}]'.format(
                            self.board.size)))
                    d = Client.recv(1024)
                    position_y = int(d.decode())
                except ValueError:
                    position_y=0

            if self.board.set_position(position_x, position_y, self.player1.sign):
                self.board.is_winner(Client, self.player0)
                return True
            else:
                return False
