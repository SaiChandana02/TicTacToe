from uuid import uuid4
from player import Player
import random
from Board import Board

@staticmethod
    def playGame():
        if newGame!=None:
            return newGame
        newGame = Game()
        return newGame

class Game:
    players = []
    lastPayerTurn = 0
    def __init__(self):
        self.gameId =  uuid4()

    def __createPlayers(self,userName1,userName2,userSymbol1,userSymbol2):
        player1 = Player(userName1,userSymbol1)
        player2 = Player(userName2,userSymbol2) 
        if len(Game.players)!=0:
            Game.players.clear()
        Game.players.append(player1)
        Game.players.append(player2)
        return True

    def __createBoard(self):
        newBoard = Board()
        return newBoard

    def startGame(self,userName1,userName2,userSymbol1,userSymbol2):
        self.__createPlayers(userName1,userName2,userSymbol1,userSymbol2)
        randomFirstPlayerNumber = random.randint(0,1)
        firstPlayer = Game.players[randomFirstPlayerNumber]
        Game.lastPayerTurn = randomFirstPlayerNumber
        newBoard = self.__createBoard()
        firstPlayer.markCell(newBoard,0,0)
        
        while(newBoard.checkForDraw()==False and newBoard.resultAnalyzer()==False):
            newBoard.printBoard()
            nextTurn = int(not Game.lastPayerTurn)
            print(str(nextTurn)+"Th Player enter you choise index to continue!!")
            indexI = int(input("Enter the row index: "))
            indexJ = int(input("Enter the column index: "))
            nextPlayer = Game.players[nextTurn]
            nextPlayer.markCell(newBoard,indexI,indexJ)
            Game.lastPayerTurn = nextTurn

        if newBoard.checkForDraw()==True:
            print("Game Draw!!")
        elif newBoard.resultAnalyzer():
            print("WIN!!")
        

#driver code

newGame = Game()
newGame.startGame("s","p","X","O")
           


            







