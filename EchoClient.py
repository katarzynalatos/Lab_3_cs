import socket


class EchoClient:
    def __init__(self, address, port, data_size):
        self.data_size=data_size
        self._create_socket()
        self._connect_to_server(address,port)
        self.send_message()

    def send_message(self):
        while True:
            response = self.sock.recv(1024)
            print(response.decode())
            if "disconnected" in response.decode():
                self.sock.close()
                break
            message = ""
            while len(message)==0:
                message = input()
            if message=="END":
                print('Successfully disconnected\n')
                self.sock.close()
                break
            self.sock.send(str.encode(message))


    def _create_socket(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def _connect_to_server(self,address,port):
        server_address=(address,port)
        print("Connecting to port:  "+str(port))
        self.sock.connect(server_address)

if __name__=="__main__":
    host='localhost'
    port=42012
    data_size=1024
    server=EchoClient(host, port,data_size)


