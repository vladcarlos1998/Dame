from obiecte.Dama import dama
from obiecte.Move import move_dama
from Repository.RepoDame import repo_dame

class ser_dame:
    def __init__(self, repo):
        self.__repo = repo
        self.__table = [["0", "0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0", "0"], ["0", "0", "0", "0", "0", "0", "0", "0"]]

    def set_table(self):
        try:
            f = open("SaveFile","r")
        except IOError:
            return []
        line = f.readline().split()
        if len(line) == 0:
            self.__repo.init_form_table()
        else:
            self.__repo.init_save_table()
        f.close()

        for d in self.__repo.findAll():
            self.__table[d.get_pozR()][d.get_pozC()] = d.get_tip()

    def save_table_file(self):
        f = open("SaveFile", "w")
        f.write("")
        f.close()

        f = open("SaveFile", "a")
        i = 0
        while i < 8:
            f.write(self.__table[i][0] + " " + self.__table[i][1] + " " + self.__table[i][2] + " " + self.__table[i][3] + " " + self.__table[i][4] + " " + self.__table[i][5] + " " + self.__table[i][6] + " " + self.__table[i][7] + "\n")
            i = i + 1
        f.write(str(self.__repo.get_curentP()))
        f.close()

    def remove(self, pozR, pozC):
        d = dama("no", pozR, pozC)
        self.__repo.remove_dame(d)
        self.__table[pozR][pozC] = "0"
        self.save_table_file()

    def upd(self, pozR_o, pozC_o, pozR_n, pozC_n):
        d = self.__repo.findOne(pozR_o, pozC_o)
        dd = dama("no", pozR_n, pozC_n)
        self.__repo.upd_dame(d, dd)
        self.__table[pozR_o][pozC_o] = "0"
        self.__table[pozR_n][pozC_n] = d.get_tip()
        self.save_table_file()

    def findOne_dama(self, pozR, pozC):
        return self.__repo.findOne(pozR, pozC)

    def findAll_dame(self):
        return self.__repo.findAll()

    def size(self):
        return len(self.__repo)

    def __str__(self):
        s = "    0 1 2 3 4 5 6 7\n\n"
        i = 0
        while i < 8:
            s = s + str(i) + "   " + self.__table[i][0] + " " + self.__table[i][1] + " " + self.__table[i][2] + " " + self.__table[i][
                3] + " " + self.__table[i][4] + " " + self.__table[i][5] + " " + self.__table[i][6] + " " + self.__table[i][7] + "\n"
            i = i + 1
        return s

    def normal_move_d(self, dama):
        list = []
        if dama.get_pozR() - 1 >= 0 and dama.get_pozC() - 1 >= 0 and self.__table[dama.get_pozR() - 1][dama.get_pozC() - 1] == "0":
            list.append(move_dama(dama.get_pozR() - 1, dama.get_pozC() - 1))
        if dama.get_pozR() - 1 >= 0 and dama.get_pozC() + 1 < 8 and self.__table[dama.get_pozR() - 1][dama.get_pozC() + 1] == "0":
            list.append(move_dama(dama.get_pozR() - 1, dama.get_pozC() + 1))
        if dama.get_pozR() + 1 < 8 and dama.get_pozC() + 1 < 8 and self.__table[dama.get_pozR() + 1][dama.get_pozC() + 1] == "0":
            list.append(move_dama(dama.get_pozR() + 1, dama.get_pozC() + 1))
        if dama.get_pozR() + 1 < 8 and dama.get_pozC() - 1 >= 0 and self.__table[dama.get_pozR() + 1][dama.get_pozC() - 1] == "0":
            list.append(move_dama(dama.get_pozR() + 1, dama.get_pozC() - 1))

        return list

    def eat_move_d(self, dama):
        list = []
        if dama.get_pozR() - 2 >= 0 and dama.get_pozC() - 2 >= 0 and self.__table[dama.get_pozR() - 2][dama.get_pozC() - 2] == "0" and self.__table[dama.get_pozR() - 1][dama.get_pozC() - 1] != "0":
            list.append(move_dama(dama.get_pozR() - 2, dama.get_pozC() - 2))
        if dama.get_pozR() - 2 >= 0 and dama.get_pozC() + 2 < 8 and self.__table[dama.get_pozR() - 2][dama.get_pozC() + 2] == "0" and self.__table[dama.get_pozR() - 1][dama.get_pozC() + 1] != "0":
            list.append(move_dama(dama.get_pozR() - 2, dama.get_pozC() + 2))
        if dama.get_pozR() + 2 < 8 and dama.get_pozC() + 2 < 8 and self.__table[dama.get_pozR() + 2][dama.get_pozC() + 2] == "0" and self.__table[dama.get_pozR() + 1][dama.get_pozC() + 1] != "0":
            list.append(move_dama(dama.get_pozR() + 2, dama.get_pozC() + 2))
        if dama.get_pozR() + 2 < 8 and dama.get_pozC() - 2 >= 0 and self.__table[dama.get_pozR() + 2][dama.get_pozC() - 2] == "0" and self.__table[dama.get_pozR() + 1][dama.get_pozC() - 1] != "0":
            list.append(move_dama(dama.get_pozR() + 2, dama.get_pozC() - 2))

        return list

    def curentP(self):
        return self.__repo.get_curentP()
    def curentPmod(self):
        if self.__repo.get_curentP() == 1:
            self.__repo.set_curentP(2)
        else:
            self.__repo.set_curentP(1)