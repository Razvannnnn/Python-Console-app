from domain.note import Note
from utils import Utils

class ServiceNote:
    def __init__(self, repo_prob, repo_stud, repo_note, valid_prob, valid_stud, valid_note):
        self.__repo_prob = repo_prob
        self.__repo_stud = repo_stud
        self.__repo_note = repo_note
        self.__valid_prob = valid_prob
        self.__valid_stud = valid_stud
        self.__valid_note = valid_note

    def adaugare(self, id_student, nr_lab_prob, nota):
        """
        Asigneaza o nota unui student la o anumita problema
        :param id_student: int unic
        :param nr_lab_prob: str
        :param nota: int >=0 <11
        :return:
        """
        self.__repo_stud.exista_id_student(id_student)
        self.__repo_prob.exista_nr_lab_prob(nr_lab_prob)
        nota = Note(id_student, nr_lab_prob, nota)
        self.__valid_note.validare(nota)
        self.__repo_note.adaugare(nota)

    def modificare(self, id_student, nr_lab_prob, nota):
        """
        Modifica o notare
        :param id_student: int unic
        :param nr_lab_prob: str
        :param nota: int >=0 <11
        :return:
        """
        nota = Note(id_student, nr_lab_prob, nota)
        self.__valid_note.validare(nota)
        self.__repo_note.modificare(nota)

    def stergere(self, id_student, nr_lab_prob):
        """
        Sterge o notare
        :param id_student: int unic
        :param nr_lab_prob: str
        :return:
        """
        self.__repo_note.stergere(id_student, nr_lab_prob)


    def medie_sub_5(self):
        """
        Creeaza o lista in care media notelor studentilor este mai mica de 5
        :return: lista cu studentii cu media sub 5
        """
        studenti = self.__repo_stud.get_all()
        lista = []
        for i in studenti:
            if self.__repo_note.medie(studenti[i].get_id_student()) < 5:
                lista.append([studenti[i].get_id_student(), self.__repo_note.medie(studenti[i].get_id_student())])
        return lista

    def cmp_nume(self, x, y):
        """
        Functie de comparare a 2 note
        :param x:
        :param y:
        :return: 1 sau 0
        """
        if x[0] == y[0]:
            if x[1] > y[1]:
                return 1
            else:
                return 0
        if x[0] < y[0]:
            return 1
        return 0

    def sort_nume(self, nr_lab_prob):
        """
        Sorteaza lista de studenti dupa nume
        :return: lista noua
        """
        values = self.__repo_note.get_all()
        values_list = list(values)
        lista = []
        for nota in values_list:
            if nota.get_nr_lab_prob() == nr_lab_prob:
                student = self.__repo_stud.cautare(nota.get_id_student())
                nota.set_nume(student.get_nume())
                lista.append([nota.get_nume(), nota.get_nota()])

        #studenti_ord = Utils.insertion_sort(lista, key=lambda x: x, cmp= lambda x,y: self.cmp_nume(x,y))
        studenti_ord = Utils.comb_sort(lista, key=lambda x: x, cmp= lambda x,y: self.cmp_nume(x,y))
        #studenti_ord = sorted(lista, key=lambda x: x.get_nume())

        return studenti_ord

    def cmp_note(self, x, y):
        """
        Functie de comparare a 2 note
        :param x:
        :param y:
        :return: 1 sau 0
        """
        if x[1] == y[1]:
            if x[0] < y[0]:
                return 1
            else:
                return 0
        if x[1] > y[1]:
            return 1
        return 0

    def sort_note(self, nr_lab_prob):
        """
        Creeaza o lista noua in care notele sunt sortate
        :return: lista noua
        """
        values = self.__repo_note.get_all()
        values_list = list(values)
        lista = []
        for nota in values_list:
            if nota.get_nr_lab_prob() == nr_lab_prob:
                student = self.__repo_stud.cautare(nota.get_id_student())
                nota.set_nume(student.get_nume())
                lista.append([nota.get_nume(), nota.get_nota()])

        # studenti_ord = Utils.insertion_sort(lista, key=lambda x: x, cmp=lambda x, y: self.cmp_note(x, y))
        studenti_ord = Utils.comb_sort(lista, key=lambda x: x, cmp=lambda x, y: self.cmp_note(x, y))
        # studenti_ord = sorted(lista, key=lambda x: x.get_nume())

        return studenti_ord