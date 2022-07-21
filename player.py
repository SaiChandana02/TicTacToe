
class Player:
    def __init__(self,userName,userSymbol):
        self.userName = userName
        self.userSymbol = userSymbol

    def markCell(self,board,i,j):
        board.setCell(i,j,self.userSymbol)
        return True

    
