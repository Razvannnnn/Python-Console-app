from domain.note import Note
from utils import Utils

class RepoNota:
    def __init__(self):
        self._note = []

    def adaugare(self, nota):
        """
        Adauga o nota la lista cu note
        :param nota: obiect
        :return:
        """
        for i in self._note:
            if i.get_id_student() == nota.get_id_student() and i.get_nr_lab_prob() == nota.get_nr_lab_prob():
                raise Exception("Nota existenta!")
        self._note.append(nota)

    def modificare(self, nota):
        """
        Modifica o nota din lista cu note
        :param nota: obiect
        :return:
        """
        ok=0
        for i in range(len(self._note)):
            if self._note[i].get_id_student() == nota.get_id_student() and self._note[i].get_nr_lab_prob() == nota.get_nr_lab_prob():
                self._note[i] = nota
                ok=1
        if ok==0:
            raise Exception("Nu a fost asignata aceasta problema la acest student")


    def stergere(self, id_student, nr_lab_prob):
        """
        Sterge o nota din lita cu note
        :param id_student: int unic
        :param nr_lab_prob: str
        :return:
        """
        for i in range(len(self._note)):
            if self._note[i].get_id_student() == id_student and self._note[i].get_nr_lab_prob() == nr_lab_prob:
                del self._note[i]
                return

    def nota(self, id_student, nr_lab_prob):
        """
        Returneaza nota unui student id_student de la o anumita problema nr_lab_prob
        :param id_student: int unic
        :param nr_lab_prob: str
        :return: nota
        """
        for i in range(len(self._note)):
            if self._note[i].get_id_student() == id_student and self._note[i].get_nr_lab_prob() == nr_lab_prob:
                return self._note[i].get_nota()
    '''
    def cmp_note(self, x, y):
        """
        Functie de comparare a 2 note
        :param x:
        :param y:
        :return: 1 sau 0
        """
        if x.get_nota() == y.get_nota():
            if x.get_nume() < y.get_nume():
                return 1
            else:
                return 0
        if x.get_nota() < y.get_nota:
            return 1
        return 0

    def sort_note(self):
        """
        Creeaza o lista noua in care notele sunt sortate
        :return: lista noua
        """
        #note_ord = sorted(self._note, key=lambda x: x.get_nota(), reverse=True)
        #note_ord = Utils.insertion_sort(self._note, key=lambda x: x.get_nota(), reverse=True)
        note_ord = Utils.comb_sort(self._note, key=lambda x: x.get_nota(), reverse=True)
        return note_ord
        
    '''

    def medie(self, id_student):
        """
        Returneaza media notelor unui student cu id_student
        :param id_student: int unic
        :return: medie
        """
        sum=0
        k=0
        for i in range(len(self._note)):
            if self._note[i].get_id_student() == id_student:
                sum += self._note[i].get_nota()
                k += 1
        if k==0:
            return 0
        else:
            return (sum//k)

    def get_all(self):
        """
        Returneaza lista de note
        :return: lista
        """
        return self._note



class FileRepoNota(RepoNota):
    def __init__(self, cale_fisier):
        RepoNota.__init__(self)
        self.__cale_fisier = cale_fisier

    def __read_all_studenti_from_file(self):
        with open(self.__cale_fisier, "r") as f:
            self._note.clear()
            lines = f.readlines()
            for line in lines:
                if line != "":
                    parts = line.split(",")
                    id_student = int(parts[0])
                    nr_lan_prob = parts[1]
                    nota = int(parts[2])
                    notaf = Note(id_student, nr_lan_prob, nota)
                    self._note.append(notaf)

    def __write_all_studenti_to_file(self):
        with open(self.__cale_fisier, "w") as f:
            for i in self._note:
                f.write(str(i) + "\n")

    def adaugare(self, nota):
        self.__read_all_studenti_from_file()
        RepoNota.adaugare(self, nota)
        self.__write_all_studenti_to_file()

    def stergere(self, id_student, nr_lab_prob):
        self.__read_all_studenti_from_file()
        RepoNota.stergere(self, id_student, nr_lab_prob)
        self.__write_all_studenti_to_file()

    def modificare(self, nota):
        self.__read_all_studenti_from_file()
        RepoNota.modificare(self, nota)
        self.__write_all_studenti_to_file()

    def medie(self, id_student):
        self.__read_all_studenti_from_file()
        return RepoNota.medie(self, id_student)

    def nota(self, id_student, nr_lab_prob):
        self.__read_all_studenti_from_file()
        return RepoNota.nota(self, id_student, nr_lab_prob)

    def get_all(self):
        self.__read_all_studenti_from_file()
        return RepoNota.get_all(self)
