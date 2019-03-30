class move_dama:
    def __init__(self, pozR, pozC):
        self.__pozC = pozC
        self.__pozR = pozR

    def get_pozR(self):
        return self.__pozR
    def set_pozR(self, pozR):
        self.__pozR = pozR

    def get_pozC(self):
        return self.__pozC
    def set_pozC(self, pozC):
        self.__pozC = pozC

    def __str__(self):
        return str(self.__pozR) + "    " + str(self.__pozC)