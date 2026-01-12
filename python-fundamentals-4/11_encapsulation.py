class Account:
    def __init__(self, bal):
        self.__bal = bal
    def show(self):
        print(self.__bal)

a = Account(1000)
a.show()
