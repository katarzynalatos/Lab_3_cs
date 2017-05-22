import logging

def PlayGame(Client):
    Client.send(str.encode('Connected successfully\n\n 1 Play GOMOKU\n 2 Play MORE-LESS\n 3 Exit\n\n\nType "END" to exit in any time'))
    d = Client.recv(1024)
    try:
        to_return = int(d.decode())
    except ValueError:
        to_return = PlayGame(Client)
        logging.info("Player typed incorrect data.")
    return to_return
