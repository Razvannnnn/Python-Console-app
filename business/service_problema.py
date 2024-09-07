from domain.problema import Problema

class ServiceProblema:
    def __init__(self, repo_problema, valid_problema):
        self.__repo_problema = repo_problema
        self.__valid_problema = valid_problema

    def adaugare(self, nr_lab_prob, descriere, deadline):
        """
        Adauga o problema in lista de probleme
        :param nr_lab_prob: str
        :param descriere: str
        :param deadline: int >0 <32
        :return:
        """
        problema = Problema(nr_lab_prob, descriere, deadline)
        self.__valid_problema.validare(problema)
        self.__repo_problema.adaugare(problema)

    def modificare(self, nr_lab_prob, descriere, deadline):
        """
        Modifica o problema din lista de probleme
        :param nr_lab_prob: str
        :param descriere: str
        :param deadline: int >0 <32
        :return:
        """
        problema = Problema(nr_lab_prob, descriere, deadline)
        self.__valid_problema.validare(problema)
        self.__repo_problema.modificare(problema)

    def cautare(self, nr_lab_prob):
        """
        Cauta o problema cu nr_lab_prob
        :param nr_lab_prob: str
        :return: problema cu nr_lab_prob
        """
        self.__valid_problema.validare_nr_lab_prob(nr_lab_prob)
        return self.__repo_problema.cautare(nr_lab_prob)

    def stergere(self, nr_lab_prob):
        """
        Sterge o problema cu nr_lab_prob
        :param nr_lab_prob: str
        :return:
        """
        self.__valid_problema.validare_nr_lab_prob(nr_lab_prob)
        self.__repo_problema.stergere(nr_lab_prob)

    def exista_nr_lab_prob(self, nr_lab_prob):
        """
        Verifica daca exista o problema cu nr_lab_prob
        :param nr_lab_prob: str
        :return: True sau False
        """
        self.__valid_problema.validare_nr_lab_prob(nr_lab_prob)
        return self.__repo_problema.exista_nr_lab_prob(nr_lab_prob)

    def get_all(self):
        """
        Returneaza lista de probleme
        :return: lista de probleme
        """
        return self.__repo_problema.get_all()
