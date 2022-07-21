
from Board import Board
from cell import cell
import pytest

newBoard = Board()
for i in range(0,3):
    newBoard.board[0][i].mark = "X"
newBoard.board[1][0].mark = "O"
newBoard.board[1][1].mark = "O"
newBoard.board[1][2].mark = "X"
newBoard.board[2][0].mark = "O"
newBoard.board[2][1].mark = "X"
newBoard.board[2][2].mark = "O"

def test_first():
   flag =  newBoard.resultAnalyzer()
   assert flag ==True

def test_second():
    flag = newBoard.resultAnalyzer()
    assert flag == False













