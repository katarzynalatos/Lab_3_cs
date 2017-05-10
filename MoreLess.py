from random import randint

class MoreLess:
    def __init__(self):
        self.value=0
        self.more=-1
        self.number=0

    def MoreLess(self, Client):
        Client.send(str.encode("\nM O R E  L E S S\nWhat is your name?"))
        d = Client.recv(1024)
        self._name = d.decode()
        while len(self._name) == 0:
            Client.send(str.encode("Incorrect data.Type your name again\n"))
            d = Client.recv(1024)
            self._name = d.decode()
        self.number = randint(0,1000+1)
        self.value=0
        self.more=-1
        while True:
            try:
                if self.more==-1:
                    Client.send(str.encode('{} guess my value between 1 and 1000...'.format(self._name)))
                    d = Client.recv(1024)
                    self.value = int(d.decode())
                elif self.more==1:
                    Client.send(str.encode('{} my value is LESS than {}. Guess value between 1 and 1000...'.format(self._name,self.value)))
                    d = Client.recv(1024)
                    self.value = int(d.decode())
                elif self.more == 0:
                    Client.send(str.encode('{} my value is MORE than {}. Guess value between 1 and 1000...'.format(self._name, self.value)))
                    d = Client.recv(1024)
                    self.value = int(d.decode())
                elif self.more==2:
                    Client.send(str.encode('Incorrect data. {} guess value between 1 and 1000'.format(self._name)))
                    d = Client.recv(1024)
                    self.value = int(d.decode())
            except ValueError:
                self.more=2
                continue
            if self.value>self.number:
                self.more=1
                continue
            elif self.value<self.number:
                self.more=0
                continue
            elif self.value==self.number :
                Client.send(str.encode("Good job, my value was: "+str(self.number)+"\n\nSuccessfully disconnected\n"))

