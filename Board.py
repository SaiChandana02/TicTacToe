from cell import cell

class Board:
    def __init__(self):
        self.board = []
        for i in range (0,3):
            row = []
            for j in range(0,3):
                row.append(cell())
            self.board.append(row)

    def setCell(self,i,j,symbol):
        self.board[i][j].mark = symbol

    def printBoard(self):
        for i in range(0,3):
            for j in range(0,3):
                print(self.board[i][j].mark,end = " ")
            print("\n")
            

    def checkForDraw(self):
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j].mark== "-1":
                    return False
        return True
    
    def resetBoard(self):
        for i in range(0,2):
            for j in range(0,2):
                self.board[i][j].mark = "-1"
    
    
    def resultAnalyzer(self):
        # check every row 
        for i in range(0,3):
            if (self.board[i][0].mark==self.board[i][1].mark==self.board[i][2].mark) and (self.board[i][0].mark!="-1"):
                return True,self.board[i][0].mark

        #check every column

        for i in range (0,3):
            if self.board[0][i].mark==self.board[1][i].mark==self.board[2][i].mark and self.board[0][i].mark!="-1":
                return True,self.board[0][i].mark
        
        #check every diagonal

        if self.board[0][0].mark==self.board[1][1].mark==self.board[2][2].mark and self.board[0][0].mark!="-1":
            return True,self.board[0][0].mark

        return False

    
