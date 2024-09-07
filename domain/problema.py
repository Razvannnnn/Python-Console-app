class Problema:
    def __init__(self, nr_lab_prob, descriere, deadline):
        self.__nr_lab_prob = nr_lab_prob
        self.__descriere = descriere
        self.__deadline = deadline

    def get_nr_lab_prob(self):
        return self.__nr_lab_prob

    def get_descriere(self):
        return self.__descriere

    def get_deadline(self):
        return self.__deadline

    def set_nr_lab_prob(self, nr_lab_prob):
        self.__nr_lab_prob = nr_lab_prob

    def set_descriere(self, descriere):
        self.__descriere = descriere

    def set_deadline(self, deadline):
        self.__deadline = deadline

    def __str__(self):
        return (f"{self.__nr_lab_prob}\n"
                f"{self.__descriere}\n"
                f"{self.__deadline}")