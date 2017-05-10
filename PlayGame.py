
def PlayGame(Client):
    Client.send(str.encode("Connected successfully\n\n 1 Play GOMOKU\n 2 Play MORE-LESS\n 3 Exit"))
    d = Client.recv(1024)
    to_return = int(d.decode())
    return to_return
