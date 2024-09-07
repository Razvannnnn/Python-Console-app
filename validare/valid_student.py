from domain.student import Student

class ValidStudent:
    def validare(self, student):
        """
        Verifica daca student are variabile valide
        :param student: obiect
        :return:
        """
        erori = ""
        if student.get_id_student() <= 0:
            erori += "ID student invalid!\n"
        if student.get_nume() == "":
            erori += "Nume student invalid!\n"
        if student.get_grup() <= 0:
            erori += "Grup student invalid!\n"
        if len(erori) > 0:
            raise Exception(erori)

    def validare_id_student(self, id_student):
        """
        Verifica daca id_student este valid
        :param id_student: int unic
        :return:
        """
        erori = ""
        if id_student <= 0:
            erori += "ID student invalid!\n"
        if len(erori) > 0:
            raise Exception(erori)