from domain.problema import Problema

class RepoProblema:
    def __init__(self):
        self._probleme = {

        }

    def adaugare(self, problema):
        """
        Adauga o problema la lista cu probleme
        :param problema: obiect
        :return:
        """
        nr_lab_prob = problema.get_nr_lab_prob()
        if nr_lab_prob in self._probleme:
            raise Exception("Problema existenta!")
        self._probleme[nr_lab_prob] = problema

    def modificare(self, problema):
        """
        Modifica o problema din lista cu probleme
        :param problema: obiect
        :return:
        """
        nr_lab_prob = problema.get_nr_lab_prob()
        if nr_lab_prob not in self._probleme:
            raise Exception("Problema inexistenta!")
        self._probleme[nr_lab_prob] = problema

    def cautare(self, nr_lab_prob):
        """
        Returneaza o problema din lista de probleme
        :param nr_lab_prob: obiect
        :return:
        """
        if nr_lab_prob not in self._probleme:
            raise Exception("Problema inexistenta!")
        return self._probleme[nr_lab_prob]

    def stergere(self, nr_lab_prob):
        """
        Sterge o problema din lista de probleme
        :param nr_lab_prob: obiect
        :return:
        """
        if nr_lab_prob not in self._probleme:
            raise Exception("Problema inexistenta!")
        del self._probleme[nr_lab_prob]

    def exista_nr_lab_prob(self, nr_lab_prob):
        """
        Verifica daca exista in lista de probleme o problema cu nr_lab_prob
        :param nr_lab_prob: str
        :return: True sau False
        """
        if nr_lab_prob not in self._probleme:
            raise Exception("Problema inexistenta")
        return True

    def get_all(self):
        """
        Returneaza toata lista de probleme
        :return: lista de probleme
        """
        return self._probleme


class FileRepoProbleme(RepoProblema):
    def __init__(self, cale_fisier):
        RepoProblema.__init__(self)
        self.__cale_fisier = cale_fisier

    def __read_all_probleme_from_file(self):
        with open(self.__cale_fisier, "r") as f:
            self._probleme.clear()
            lines = f.readlines()
            num_lines = len(lines)
            for i in range(0, num_lines, 3):
                nr_lab_prob = lines[i].strip()
                descriere = lines[i+1].strip()
                deadline = int(lines[i+2].strip())
                prob = Problema(nr_lab_prob, descriere, deadline)
                self._probleme[nr_lab_prob] = prob
            """
            for line in lines:
                if line != "":
                    parts = line.split()
                    nr_lab_prob = parts[0]
                    descriere = parts[1]
                    deadline = int(parts[2])
                    prob = Problema(nr_lab_prob, descriere, deadline)
                    self._probleme[nr_lab_prob] = prob
            """

    def __write_all_probleme_to_file(self):
        with open(self.__cale_fisier,"w") as f:
            for nr_lab_prob in self._probleme:
                f.write(str(self._probleme[nr_lab_prob])+"\n")

    def adaugare(self, problema):
        self.__read_all_probleme_from_file()
        RepoProblema.adaugare(self, problema)
        self.__write_all_probleme_to_file()

    def modificare(self, problema):
        self.__read_all_probleme_from_file()
        RepoProblema.modificare(self, problema)
        self.__write_all_probleme_to_file()

    def cautare(self, nr_lab_prob):
        self.__read_all_probleme_from_file()
        return RepoProblema.cautare(self, nr_lab_prob)

    def stergere(self, nr_lab_prob):
        self.__read_all_probleme_from_file()
        RepoProblema.stergere(self, nr_lab_prob)
        self.__write_all_probleme_to_file()

    def exista_nr_lab_prob(self, nr_lab_prob):
        self.__read_all_probleme_from_file()
        return RepoProblema.exista_nr_lab_prob(self, nr_lab_prob)

    def get_all(self):
        self.__read_all_probleme_from_file()
        return RepoProblema.get_all(self)