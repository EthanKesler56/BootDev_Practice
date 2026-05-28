class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if num <= 0: 
            raise Exception("Not enough arrows")
        else: 
            num -= 1


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name,num_arrows)

    def triple_shot(self, target):
        num_arrows -= 3
        