from domain.note import Note
class ValidNota:
    def validare(self, nota):
        """
        Verifica daca nota are variabile valide
        :param nota: obiect
        :return:
        """
        erori = ""
        if nota.get_id_student() <= 0:
            erori += "Student invalid!"
        if nota.get_nr_lab_prob() == "":
            erori += "Nr lab prob invalid!"
        if nota.get_nota() < 0 or nota.get_nota() > 10:
            erori += "Nota invalida!"
        if len(erori) > 0:
            raise Exception(erori)