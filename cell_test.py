import pytest

from cell import cell

newCell = cell()

def test_first():
   flag =  newCell.isMarked()
   assert flag==False


def test_second():
    newCell.mark = "X"
    flag = newCell.isMarked()
    assert flag==True

def test_third():
    newCell.mark="O"
    flag = newCell.isMarked()
    assert flag==True

def test_fourth():
    newCell.mark = "abc"
    flag = newCell.isMarked()
    assert flag == False


