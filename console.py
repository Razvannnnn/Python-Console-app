from domain.student import Student
from domain.problema import Problema
from domain.note import Note

class UI:
    def __init__(self, srv_student, srv_problema, srv_nota):
        self.__srv_student = srv_student
        self.__srv_problema = srv_problema
        self.__srv_nota = srv_nota
        self.__comenzi = {
            "add_student":self.__ui_add_student,
            "add_problema":self.__ui_add_problema,
            "modif_student":self.__ui_modif_student,
            "modif_problema":self.__ui_modif_problema,
            "cauta_student":self.__ui_cauta_student,
            "cauta_problema":self.__ui_cauta_problema,
            "del_student":self.__ui_del_student,
            "del_problema":self.__ui_del_problema,
            "print_studenti":self.__ui_print_studenti,
            "print_problema":self.__ui_print_probleme,
            "generate_student":self.__ui_generate_student,
            "asign_nota":self.__ui_asign_nota,
            "asign_problema":self.__ui_asign_problema,
            "modif_nota":self.__ui_modif_nota,
            "sterge_nota":self.__ui_sterge_nota,
            "sort_note":self.__ui_sort_note,
            "sort_nume":self.__ui_sort_nume,
            "medie_sub_5":self.__ui_medie_sub_5
        }

    def __ui_sort_note(self, params):
        if len(params) != 1:
            print("Nr parametri invalid!")
            return
        try:
            nr_lab_prob = params[0]
            list = self.__srv_nota.sort_note(nr_lab_prob)
            if not list:
                print("Nu exista studenti care sa aiba note la aceasta problema")
            else:
                print(f"Note {nr_lab_prob}:")
                for i in list:
                    print(f"Nume:{i[0]} Nota:{i[1]}")
        except Exception as ex:
            print(ex)

    def __ui_sort_nume(self, params):
        if len(params) != 1:
            print("Nr parametri invalid!")
            return
        try:
            nr_lab_prob = params[0]
            studenti_ord = self.__srv_nota.sort_nume(nr_lab_prob)
            if not studenti_ord:
                print("Nu exista studenti care sa aiba note la aceasta problema")
            else:
                print(f"Note {nr_lab_prob}:")
                for i in studenti_ord:
                    print(f"Nume:{i[0]} Nota:{i[1]}")
        except Exception as ex:
            print(ex)

    def __ui_medie_sub_5(self, params):
        if len(params) != 0:
            print("Nr parametri invalid!")
            return
        try:
            list = self.__srv_nota.medie_sub_5()
            for i in list:
                print(f"ID:{i[0]} Media:{i[1]}")
        except Exception as ex:
            print(ex)

    def __ui_modif_nota(self, params):
        if len(params) != 3:
            print("Nr parametri invalid!")
            return
        try:
            id_student = int(params[0])
            nr_lab_prob = params[1]
            nota = int(params[2])
            self.__srv_nota.modificare(id_student, nr_lab_prob, nota)
        except Exception as ex:
            print(ex)

    def __ui_sterge_nota(self, params):
        if len(params) != 2:
            print("Nr parametri invalid!")
            return
        try:
            id_student = int(params[0])
            nr_lab_prob = params[1]
            self.__srv_nota.stergere(id_student, nr_lab_prob)
        except Exception as ex:
            print(ex)

    def __ui_add_student(self, params):
        if len(params)!=3:
            print("Nr parametri invalid!")
            return
        try:
            id_student = int(params[0])
            nume = params[1]
            grup = int(params[2])
            self.__srv_student.adaugare(id_student,nume,grup)
        except Exception as ex:
            print(ex)
    def __ui_add_problema(self, params):
        if len(params)!=3:
            print("Nr parametri invalid!")
            return
        try:
            nr_lab_prob = params[0]
            descriere = params[1]
            deadline = int(params[2])
            self.__srv_problema.adaugare(nr_lab_prob, descriere, deadline)
        except Exception as ex:
            print(ex)
    def __ui_modif_student(self, params):
        if len(params)!=3:
            print("Nr parametri invalid!")
            return
        try:
            id_student = int(params[0])
            nume = params[1]
            grup = int(params[2])
            self.__srv_student.modificare(id_student,nume,grup)
        except Exception as ex:
            print(ex)

    def __ui_modif_problema(self, params):
        if len(params)!=3:
            print("Nr parametri invalid!")
            return
        try:
            nr_lab_prob = params[0]
            descriere = params[1]
            deadline = int(params[2])
            self.__srv_problema.modificare(nr_lab_prob, descriere, deadline)
        except Exception as ex:
            print(ex)

    def __ui_cauta_student(self, params):
        if len(params)!=1:
            print("Nr parametri invalid!")
            return
        try:
            id_student = int(params[0])
            student = self.__srv_student.cautare(id_student)
            print(student)
        except Exception as ex:
            print(ex)

    def __ui_cauta_problema(self, params):
        if len(params)!=1:
            print("Nr parametri invalid!")
            return
        try:
            nr_lab_prob = params[0]
            problema = self.__srv_problema.cautare(nr_lab_prob)
            print(problema)
        except Exception as ex:
            print(ex)

    def __ui_del_student(self, params):
        if len(params)!=1:
            print("Nr parametri invalid!")
            return
        try:
            id_student = int(params[0])
            self.__srv_student.stergere(id_student)
        except Exception as ex:
            print(ex)


    def __ui_del_problema(self, params):
        if len(params)!=1:
            print("Nr parametri invalid!")
            return
        try:
            nr_lab_prob = params[0]
            self.__srv_problema.stergere(nr_lab_prob)
        except Exception as ex:
            print(ex)

    def __ui_print_studenti(self, params):
        if len(params)!=0:
            print("Nr parametri invalid!")
            return
        try:
            studenti = self.__srv_student.get_all()
            for i in studenti:
                print(studenti[i])
        except Exception as ex:
            print(ex)


    def __ui_print_probleme(self, params):
        if len(params)!=0:
            print("Nr parametri invalid!")
            return
        try:
            probleme = self.__srv_problema.get_all()
            for i in probleme:
                print(probleme[i])
        except Exception as ex:
            print(ex)

    def __ui_generate_student(self, params):
        if len(params)!=1:
            print("Nr parametri invalid!")
            return
        try:
            nr_studenti = int(params[0])
            self.__srv_student.generate_random_student(nr_studenti)
            print(f"Au fost generati {nr_studenti} studenti")
        except Exception as ex:
            print(ex)

    def __ui_asign_problema(self, params):
        if len(params) != 2:
            print("Nr parametri invalid!")
            return
        try:
            id_student = int(params[0])
            nr_lab_prob = params[1]
            nota = 0
            self.__srv_nota.adaugare(id_student, nr_lab_prob, nota)
        except Exception as ex:
            print(ex)

    def __ui_asign_nota(self, params):
        if len(params) != 3:
            print("Nr parametri invalid!")
            return
        try:
            id_student = int(params[0])
            nr_lab_prob = params[1]
            nota = int(params[2])
            self.__srv_nota.modificare(id_student, nr_lab_prob, nota)
        except Exception as ex:
            print(ex)


    def run(self):
        while True:
            comanda = input(">>>")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return
            parts = comanda.split()
            comanda_name = parts[0]
            params = parts[1:]
            if comanda_name in self.__comenzi:
                try:
                    self.__comenzi[comanda_name](params)
                except Exception as ex:
                    print(ex)
            else:
                print("Comanda invalida!")