import socket
from Gomoku import Gomoku
from PlayGame import PlayGame
from MoreLess import MoreLess
import logging
import os


class EchoServer:
    def __init__(self, address, port, data_size):
        self.data_size=data_size
        self._create_socket()
        self._bind_socket(address,port)
        if os.path.isfile("Logs.log"):
            os.unlink("Logs.log")
        logging.basicConfig(filename="Logs.log",level=logging.INFO)

    def about_connection(self):
        self.sock.listen()
        connection, client_address=self.sock.accept()
        logging.info("Player no" + str(client_address) + " successfully connected.")
        while True:
            self.decision=PlayGame(connection)
            if self.decision == 1:
                self.decision = 0
                logging.info("Player no "+str(client_address)+" chose Gomoku game.")
                new_game = Gomoku()
                new_game.Gomoku(connection)
                break
            elif self.decision==2:
                self.decision = 0
                logging.info("Player no " + str(client_address) + " chose More Less game.")
                new_game2 = MoreLess()
                new_game2.MoreLess(connection)
                break
            elif self.decision == 3:
                connection.send(str.encode('Successfully disconnected'))
                logging.info("Player no " + str(client_address) + " successfully disconnected.")
                logging.shutdown()
                connection.close()
                break

    def _create_socket(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def _bind_socket(self,address,port):
        server_address=(address,port)
        self.sock.bind(server_address)

if __name__=="__main__":
    host='localhost'
    port=42012
    data_size=1024
    server=EchoServer(host, port,data_size)
    server.about_connection()
