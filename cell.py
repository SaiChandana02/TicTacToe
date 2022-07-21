class cell:
    def __init__(self):
        self.mark = "-1"

    def isMarked(self)->bool:
        return  self.mark=="X" or self.mark=="O"
    