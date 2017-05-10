import socket
from Gomoku import Gomoku
from PlayGame import PlayGame
from MoreLess import MoreLess


class EchoServer:
    def __init__(self, address, port, data_size):
        self.data_size=data_size
        self._create_socket()
        self._bind_socket(address,port)

    def about_connection(self):
        self.sock.listen()
        connection, client_address=self.sock.accept()
        new_game = Gomoku()
        new_game2 = MoreLess()
 #       new_game.Gomoku(connection)
        connection.decision=PlayGame(connection)
        if connection.decision == 1:
            connection.decision = 0
            new_game.Gomoku(connection)
        elif connection.decision==2:
            new_game2.MoreLess(connection)
            connection.decision=0
        elif connection.decision == 3:
            connection.send(str.encode('Successfully disconnected'))
            exit()
        while True:
            connection.send_message()

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
