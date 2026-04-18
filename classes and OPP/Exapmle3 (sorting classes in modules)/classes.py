class Coin:
    def __init__(self):
        self.__sideup='heads'

    def flip(self):
        if self.__sideup =='heads':
            self.__sideup='tails'
        else:
            self.__sideup='heads'

    def get_sideup(self):
        return self.__sideup
    
    def set_sideup(self,num):
        if num=='1':
            self.__sideup='heads'
        elif num=='2':
            self.__sideup='tails'





