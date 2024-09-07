class Note:
    def __init__(self, id_student, nr_lab_prob, nota):
        self.__id_student = id_student
        self.__nr_lab_prob = nr_lab_prob
        self.__nota = nota
        self.__nume = ""

    def get_id_student(self):
        return self.__id_student

    def get_nr_lab_prob(self):
        return self.__nr_lab_prob

    def get_nota(self):
        return self.__nota

    def get_nume(self):
        return self.__nume

    def set_id_student(self, id_student):
        self.__id_student = id_student

    def set_nr_lab_prob(self, nr_lab_prob):
        self.__nr_lab_prob = nr_lab_prob

    def set_nota(self, nota):
        self.__nota = nota

    def set_nume(self, nume):
        self.__nume = nume

    def __str__(self):
        return f"{self.__id_student},{self.__nr_lab_prob},{self.__nota}"