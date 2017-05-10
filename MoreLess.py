from random import randint

class MoreLess:
    def __init__(self):
        pass
    def MoreLess(self, Client):
        Client.send(str.encode("M O R E  L E S S\nWhat is your name?"))
        d = Client.recv(1024)
        self._name = d.decode()
        while len(self._name) == 0:
            Client.send(str.encode("Incorrect data.Type your name again\n"))
            d = Client.recv(1024)
            self._name = d.decode()
        self.number = randint()
        self.value=0
        more=-1
        while True:
            try:
                if more==-1:
                    Client.send(str.encode('{} guess value.'.format(self._name)))
                elif more==1:
                    Client.send(str.encode('{} my value is MORE than {}. Guess value.'.format(self._name) .format(self.value)))
                elif more == 0:
                    Client.send(str.encode('{} my value is LESS than {}. Guess value.'.format(self._name) .format(self.value)))
                d = Client.recv(1024)
                self.value = int(d.decode())
            except ValueError:
                Client.send(str.encode('Incorrect data. {} guess value'.format(self._name)))
                d = Client.recv(1024)
                self.value = int(d.decode())
            if self.value>self.number:
                more=1
            elif self.value<self.number:
                more=0
            elif self.value==self.number :
                Client.send(str.encode("Good job, my value was: "+str(self.number)+"1 Play again\n 2 Play other game\n 3 Exit"))
                d = Client.recv(1024)
                Client.decision = int(d.decode())
