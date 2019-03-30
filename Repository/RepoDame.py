from obiecte.Dama import dama

class repo_dame:
    def __init__(self):
        self.__dame = []
        self.__curentP = 1

    def init_form_table(self):
        self.__dame.append(dama("2", 0, 0))
        self.__dame.append(dama("2", 0, 2))
        self.__dame.append(dama("2", 0, 4))
        self.__dame.append(dama("2", 0, 6))
        self.__dame.append(dama("2", 1, 1))
        self.__dame.append(dama("2", 1, 3))
        self.__dame.append(dama("2", 1, 5))
        self.__dame.append(dama("2", 1, 7))

        self.__dame.append(dama("1", 7, 1))
        self.__dame.append(dama("1", 7, 3))
        self.__dame.append(dama("1", 7, 5))
        self.__dame.append(dama("1", 7, 7))
        self.__dame.append(dama("1", 6, 0))
        self.__dame.append(dama("1", 6, 2))
        self.__dame.append(dama("1", 6, 4))
        self.__dame.append(dama("1", 6, 6))

    def init_save_table(self):
        try:
            f = open("SaveFile","r")
        except IOError:
            return []
        i = 0
        while i < 8:
            line = f.readline().split()
            j = 0
            for d in line:
                if d != "0":
                    self.__dame.append(dama(d, i, j))
                j = j + 1
            i = i + 1
        line = f.readline().split()
        self.__curentP = int(line[0])
        f.close()

    def remove_dame(self, dama):
        for i in range(len(self.__dame)):
            if self.__dame[i].get_pozR() == dama.get_pozR() and self.__dame[i].get_pozC() == dama.get_pozC():
                    self.__dame.pop(i)
                    break

    def upd_dame(self, damaOld, damaNow):
        for i in range(len(self.__dame)):
            if self.__dame[i].get_pozR() == damaOld.get_pozR() and self.__dame[i].get_pozC() == damaOld.get_pozC():
                self.__dame[i].set_pozR(damaNow.get_pozR())
                self.__dame[i].set_pozC(damaNow.get_pozC())

    def findAll(self):
        return self.__dame[:]

    def __len__(self):
        return len(self.__dame)

    def findOne(self, pozR, pozC):
        for i in range(len(self.__dame)):
            if self.__dame[i].get_pozR() == pozR and self.__dame[i].get_pozC() == pozC:
                return self.__dame[i]
        return None

    def get_curentP(self):
        return self.__curentP
    def set_curentP(self, curentP):
        self.__curentP = curentP