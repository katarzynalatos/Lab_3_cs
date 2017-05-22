from GomokuStarter import GomokuStarter
from Play import Play
from Player import Player
from Board import Board
import logging

class Gomoku:
    def __init__(self):
        self.player0= Player()
        self.player1 = Player()
        self.board = Board()

    def Gomoku(self, Client):
        starter = GomokuStarter()
        starter.Start(Client)
        self.player1 = starter.return_player()
        self.board = starter.return_board()
        self.player0.sign=-(self.player1.sign)
        game = Play(self.board, self.player0, self.player1)
        correct_step=False
        player_nr=1
        while True:
            if correct_step==True and player_nr==self.player0.nr:
                player_nr=self.player1.nr
            elif correct_step==True and player_nr==self.player1.nr:
                player_nr=self.player0.nr
            logging.info("Player no: "+str(player_nr)+" played.")
            correct_step=game.play(Client,player_nr,correct_step)









