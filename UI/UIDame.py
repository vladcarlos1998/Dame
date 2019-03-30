from obiecte.Dama import dama
from Repository.RepoDame import repo_dame
from Service.ServiceDame import ser_dame
from obiecte.Move import move_dama

class UI_dame:
    def __init__(self, ser):
        self.__ser = ser

    def run(self):
        self.__ser.set_table()
        self.__ser.save_table_file()
        while True:
            print(str(self.__ser))
            print()

            while True:
                print(">>   Player " + str(self.__ser.curentP()) + " turn")
                piesa = input("Cordonate piesa: ")
                if piesa == "exit":
                    break
                ok = 1
                if len(piesa) != 2:
                    ok = 0
                if int(piesa[0]) < 0 or int(piesa[0]) > 7 or int(piesa[1]) < 0 or int(piesa[1]) > 7:
                    ok = 0
                if self.__ser.findOne_dama(int(piesa[0]), int(piesa[1])) is None:
                    ok = 0
                else:
                    if self.__ser.findOne_dama(int(piesa[0]), int(piesa[1])).get_tip() != str(self.__ser.curentP()):
                        ok = 0
                if ok == 1:
                    break
                else:
                    print()
                    print(">> Cordonate gresite <<")
                    print()

            if piesa == "exit":
                print("End Game")
                fil = open("SaveFile", "w")
                fil.write("")
                fil.close()
                break

            s = "HINT:  "
            for x in self.__ser.normal_move_d(dama(str(self.__ser.curentP()), int(piesa[0]), int(piesa[1]))):
                s = s + str(x.get_pozR()) + str(x.get_pozC()) + "   "
            for x in self.__ser.eat_move_d(dama(str(self.__ser.curentP()), int(piesa[0]), int(piesa[1]))):
                s = s + str(x.get_pozR()) + str(x.get_pozC()) + "   "
            print(s)

            while True:
                print(">>   Player " + str(self.__ser.curentP()) + " turn")
                moveto = input("Move to: ")
                ok = 1
                if len(moveto) != 2:
                    ok = 0
                if int(moveto[0]) < 0 or int(moveto[0]) > 7 or int(moveto[1]) < 0 or int(moveto[1]) > 7:
                    ok = 0
                okk = 0
                for x in self.__ser.normal_move_d(dama(str(self.__ser.curentP()), int(piesa[0]), int(piesa[1]))):
                    if x.get_pozR() == int(moveto[0]) and x.get_pozC() == int(moveto[1]):
                        okk = 1
                        break
                if okk == 0:
                    for x in self.__ser.eat_move_d(dama(str(self.__ser.curentP()), int(piesa[0]), int(piesa[1]))):
                        if x.get_pozR() == int(moveto[0]) and x.get_pozC() == int(moveto[1]):
                            okk = 2
                            break
                if okk == 0:
                    ok = 0
                if ok == 1:
                    break
                else:
                    print()
                    print(">> Cordonate gresite <<")
                    print()

            while True:
                self.__ser.upd(int(piesa[0]), int(piesa[1]), int(moveto[0]), int(moveto[1]))
                no = 0
                if int(moveto[1]) - int(piesa[1]) == 2 or int(moveto[1]) - int(piesa[1]) == -2:
                    kPozC = int(int(piesa[1]) + ((int(moveto[1]) - int(piesa[1]))/2))
                    kPozR = int(int(piesa[0]) + ((int(moveto[0]) - int(piesa[0]))/2))
                    if self.__ser.findOne_dama(kPozR, kPozC).get_tip() != self.__ser.findOne_dama(int(moveto[0]), int(moveto[1])).get_tip():
                        self.__ser.remove(kPozR, kPozC)
                    no = 1

                l = []
                if no == 1:
                    for x in self.__ser.eat_move_d(dama(str(self.__ser.curentP()), int(moveto[0]), int(moveto[1]))):
                        l.append(x)
                    i = -1
                    j = 0
                    for x in l:
                        if x.get_pozR() == int(piesa[0]) and x.get_pozC() == int(piesa[1]):
                            i = j
                            break
                        j = j + 1
                    if i != -1:
                        l.pop(i)

                if len(l) == 0:
                    self.__ser.curentPmod()
                    self.__ser.save_table_file()
                    break
                else:
                    print(str(self.__ser))
                    print()

                    piesa = moveto
                    s = "HINT:  "
                    for x in l:
                        s = s + str(x.get_pozR()) + str(x.get_pozC()) + "   "
                    print(s)

                    while True:
                        print(">>   Player " + str(self.__ser.curentP()) + " turn")
                        moveto = input("Move to: ")
                        ok = 1
                        if len(moveto) != 2:
                            ok = 0
                        if int(moveto[0]) < 0 or int(moveto[0]) > 7 or int(moveto[1]) < 0 or int(moveto[1]) > 7:
                            ok = 0
                        ook = 0
                        if ook == 0:
                            for x in l:
                                if x.get_pozR() == int(moveto[0]) and x.get_pozC() == int(moveto[1]):
                                    ook = 1
                                    break
                        if ook == 0:
                            ok = 0
                        if ok == 1:
                            break
                        else:
                            print()
                            print(">> Cordonate gresite <<")
                            print()

            alb = 0
            negru = 0
            for f in self.__ser.findAll_dame():
                if f.get_tip() == "1":
                    alb = alb + 1
                else:
                    negru = negru + 1
            if alb == 0:
                print("Player 2 WIN")
                fil = open("SaveFile", "w")
                fil.write("")
                fil.close()
                break
            else:
                print("Player 1 WIN")
                fil = open("SaveFile", "w")
                fil.write("")
                fil.close()
                break

