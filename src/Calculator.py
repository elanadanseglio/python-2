class Calculator:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.__result = 0
    
    def get_result(self):
        return self.__result
        
    def add(self):
        self.__result = self.x + self.y
    def sub(self):
        self.__result = self.x - self.y
    def mul(self):
        self.__result = self.x * self.y
    def div(self):
        self.__result = self.x / self.y
    