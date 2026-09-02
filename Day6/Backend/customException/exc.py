class MyException(Exception):
    def __init__(self,e):
        super().__init__(e)
        self.e=e