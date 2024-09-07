from domain.student import Student

class ServiceStudent:
    def __init__(self, repo_student, valid_student):
        self.__repo_student = repo_student
        self.__valid_student = valid_student

    def adaugare(self, id_student, nume, grup):
        """
        Adauga un student in lista de studenti
        :param id_student: int unic
        :param nume: str
        :param grup: int
        :return:
        """
        student = Student(id_student, nume, grup)
        self.__valid_student.validare(student)
        self.__repo_student.adaugare(student)

    def modificare(self, id_student, nume, grup):
        """
        Modifica un student in lista de studenti
        :param id_student: int unic
        :param nume: str
        :param grup: int
        :return:
        """
        student = Student(id_student, nume, grup)
        self.__valid_student.validare(student)
        self.__repo_student.modificare(student)

    def cautare(self, id_student):
        """
        Cauta studentul cu id-ul id_student si il afiseaza
        :param id_student: int unic
        :return: Studentul cu id-ul id_student
        """
        self.__valid_student.validare_id_student(id_student)
        return self.__repo_student.cautare(id_student)

    def stergere(self, id_student):
        """
        Sterge studentul cu id-ul id_student
        :param id_student: int unic
        :return:
        """
        self.__valid_student.validare_id_student(id_student)
        self.__repo_student.stergere(id_student)

    def exista_id_student(self, id_student):
        """
        Verifica daca exista studentul cu id-ul id_student
        :param id_student: int unic
        :return: True sau False
        """
        self.__valid_student.validare_id_student(id_student)
        return self.__repo_student.exista_id_student(id_student)

    def get_all(self):
        """
        Returneaza toti studentii
        :return: lista de studenti
        """
        return self.__repo_student.get_all()

    def generate_random_student(self, nr_student):
        """
        Caz favorabil O(1)
        Caz nefavorabil O(n)
        Caz mediu O(n)

        Genereaza un numar nr_student de studenti
        :param nr_student: int
        :return:
        """
        if nr_student == 0:
            return
        else:
            self.__repo_student.generate_random_student()
            self.generate_random_student(nr_student - 1)