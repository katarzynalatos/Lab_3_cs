
class Board:
    def __init__(self, size=0):
        self.size = size
        self.board = []
        for i in range(0,self.size):
            self.board.append([])
            for j in range(0, self.size):
                self.board[i].append(0)

    def is_empty(self, x, y):
        if self.board[x-1][y-1]==0:
            return True
        else:
            return False

    def set_position(self, x, y, sign, Client, player0):
        if self.board[x-1][y-1]==0:
            self.board[x-1][y-1]=sign
            self.is_winner(Client, player0)
            return True
        else:
            return False

    def check_field_horizontal(self,x,y):
        if self.size <= 5:
            winning_fields=self.size
        else:
            winning_fields=5
        """Horizontal addition"""
        sum = 0
        for field in range(0,winning_fields):
            sum+=self.board[x][y+field]
        if sum==winning_fields:
            return 1
        elif sum==-winning_fields:
            return -1

    def check_field_vertical(self, x, y):
        if self.size <= 5:
            winning_fields = self.size
        else:
            winning_fields = 5
        """Vertical addition"""
        sum = 0
        for field in range(0, winning_fields):
            sum += self.board[x+field][y]
        if sum == winning_fields:
            return 1
        elif sum == -winning_fields:
            return -1

    def check_field_cross_right(self, x, y):
        if self.size <= 5:
            winning_fields = self.size
        else:
            winning_fields = 5
        """Cross right addition"""
        sum = 0
        for field in range(0, winning_fields):
            sum += self.board[x + field][y+field]
        if sum == winning_fields:
            return 1
        elif sum == -winning_fields:
            return -1

    def check_field_cross_left(self, x, y):
        if self.size <= 5:
            winning_fields = self.size
        else:
            winning_fields = 5
        """Cross left addition"""
        sum = 0
        for field in range(0, winning_fields):
            sum += self.board[x + field][y-field]
            if y < winning_fields-1:
                raise IndexError
        if sum == winning_fields:
            return 1
        elif sum == -winning_fields:
            return -1


    def is_winner(self,Client,player0):
        end_of_game=0
        for x in range(0,self.size):
            for y in range(0,self.size):
                for function in (self.check_field_horizontal, self.check_field_vertical, self.check_field_cross_right, self.check_field_cross_left):
                    try:
                        end_of_game=function(x, y)
                    except IndexError:
                        end_of_game=0
                    if end_of_game==0:
                        continue
                    elif end_of_game==1 and player0.sign==1:
                        board=self.write_board()
                        Client.send(str.encode(board+'\nGame over.Computer won!\n\n Successfully disconnected\n'))
                    elif end_of_game==1 and player0.sign!=1:
                        board = self.write_board()
                        Client.send(str.encode(board+'\nGame over.You won!\n\n Successfully disconnected\n'))
                    elif end_of_game==-1 and player0.sign==-1:
                        board = self.write_board()
                        Client.send(str.encode(board+'\nGame over.Computer won!\n\n Successfully disconnected\n'))
                    elif end_of_game==-1 and player0.sign!=-1:
                        board = self.write_board()
                        Client.send(str.encode(board+'\nGame over.You won!\n\n Successfully disconnected\n'))


    def write_board(self):
        global_string=""
        string="   "
        for i in range(0,self.size):
            string+=str(i+1)
            string+=" "
        global_string=string+"\n"
        for i in range(0,self.size):
            string = str(i+1)
            if (i != 9):
                string += " |"
            else:
                string += "|"
            for j in range (0,self.size):
                if self.board[i][j]==1:
                    string+="O"
                elif self.board[i][j]==-1:
                    string+="X"
                else:
                    string+="_"
                string+='|'
            global_string+=string+"\n"
        return global_string

