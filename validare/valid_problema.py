class ValidProblema:
    def validare(self, problema):
        """
        Verifica daca problema are variabilele valide
        :param problema: obiect
        :return:
        """
        erori = ""
        if problema.get_nr_lab_prob() == "":
            erori += "Nr lab si prob invalid!\n"
        if problema.get_descriere() == "":
            erori += "Descriere invalida!\n"
        if problema.get_deadline() <=0 or problema.get_deadline() >= 32:
            erori += "Deadline invalid!\n"
        if len(erori) > 0:
            raise Exception(erori)

    def validare_nr_lab_prob(self, nr_lab_prob):
        """
        Verifica daca nr_lab_prob este valid
        :param nr_lab_prob: str
        :return:
        """
        erori = ""
        if nr_lab_prob == "":
            erori += "Nr lab si prob invalid!\n"
        if len(erori) > 0:
            raise Exception(erori)
