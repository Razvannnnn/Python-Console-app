from domain.student import Student
from domain.problema import Problema
from domain.note import Note
from business.service_note import ServiceNote
from business.service_student import ServiceStudent
from business.service_problema import ServiceProblema
from infrastructura.repo_student import RepoStudent
from infrastructura.repo_nota import RepoNota
from infrastructura.repo_problema import RepoProblema

class Teste:

    def __adaugare_student(self):
        id_student = 50
        nume = "Bercea"
        grup = 201
        student = Student(id_student, nume, grup)
        repo_student = RepoStudent()
        students = repo_student.get_all()
        assert len(students) == 0
        repo_student.adaugare(student)
        students = repo_student.get_all()
        assert len(students) == 1
    def __modificare_student(self):
        id_student = 50
        nume = "Bercea"
        grup = 201
        nume_2 = "Lectura"
        grup_2 = 203
        student = Student(id_student, nume, grup)
        repo_student = RepoStudent()
        students = repo_student.get_all()
        assert len(students) == 0
        repo_student.adaugare(student)
        students = repo_student.get_all()
        assert len(students) == 1
        student2 = Student(id_student, nume_2, grup_2)
        repo_student.modificare(student2)
        students = repo_student.get_all()
        assert len(students) == 1
    def __stergere_student(self):
        id_student = 50
        nume = "Bercea"
        grup = 201
        id_student_2 = 45
        nume_2 = "Lectura"
        grup_2 = 203
        student = Student(id_student, nume, grup)
        student_2 = Student(id_student_2, nume_2, grup_2)
        repo_student = RepoStudent()
        students = repo_student.get_all()
        assert len(students) == 0
        repo_student.adaugare(student)
        repo_student.adaugare(student_2)
        students = repo_student.get_all()
        assert len(students) == 2
        repo_student.stergere(id_student)
        students = repo_student.get_all()
        assert len(students) == 1
    def __adaugare_problema(self):
        nr_lab_prob = "10_3"
        descriere = "Misto"
        deadline = 30
        problema = Problema(nr_lab_prob, descriere, deadline)
        repo_problema = RepoProblema()
        probleme = repo_problema.get_all()
        assert len(probleme) == 0
        repo_problema.adaugare(problema)
        probleme = repo_problema.get_all()
        assert len(probleme) == 1

    def __modificare_problema(self):
        nr_lab_prob = "10_3"
        descriere = "Misto"
        deadline = 30
        nr_lab_prob_2 = "11_5"
        descriere_2 = "Tare"
        deadline_2 = 23
        problema = Problema(nr_lab_prob, descriere, deadline)
        problema_2 = Problema(nr_lab_prob_2, descriere_2, deadline_2)
        repo_problema = RepoProblema()
        probleme = repo_problema.get_all()
        assert len(probleme) == 0
        repo_problema.adaugare(problema)
        repo_problema.adaugare(problema_2)
        probleme = repo_problema.get_all()
        assert len(probleme) == 2
        repo_problema.stergere(nr_lab_prob)
        probleme = repo_problema.get_all()
        assert len(probleme) == 1
    def __stergere_problema(self):
        nr_lab_prob = "10_3"
        descriere = "Misto"
        deadline = 30
        descriere_2 = "Tare"
        deadline_2 = 23
        problema = Problema(nr_lab_prob, descriere, deadline)
        repo_problema = RepoProblema()
        probleme = repo_problema.get_all()
        assert len(probleme) == 0
        repo_problema.adaugare(problema)
        probleme = repo_problema.get_all()
        assert len(probleme) == 1
        problema2 = Problema(nr_lab_prob, descriere_2, deadline_2)
        repo_problema.modificare(problema2)
        probleme = repo_problema.get_all()
        assert len(probleme) == 1
    def __adaugare_nota(self):
        id_student = 1000
        nr_lab_prob = "3_2"
        nota = 7
        nota_i = Note(id_student, nr_lab_prob, nota)
        repo_nota = RepoNota()
        note = repo_nota.get_all()
        assert len(note) == 0
        repo_nota.adaugare(nota_i)
        note = repo_nota.get_all()
        assert len(note) == 1
    def __modificare_nota(self):
        id_student = 1000
        nr_lab_prob = "3_2"
        nota = 7
        nota_i = Note(id_student, nr_lab_prob, nota)
        nota2 = 5
        nota_ii = Note(id_student, nr_lab_prob, nota2)
        repo_nota = RepoNota()
        note = repo_nota.get_all()
        assert len(note) == 0
        repo_nota.adaugare(nota_i)
        note = repo_nota.get_all()
        assert len(note) == 1
        repo_nota.modificare(nota_ii)
        note = repo_nota.get_all()
        assert len(note) == 1

    def __stergere_nota(self):
        id_student = 1000
        nr_lab_prob = "3_2"
        nota = 7
        nota_i = Note(id_student, nr_lab_prob, nota)
        id_student2 = 1001
        nr_lab_prob2 = "3_3"
        nota2 = 5
        nota_ii = Note(id_student2, nr_lab_prob2, nota2)
        repo_nota = RepoNota()
        note = repo_nota.get_all()
        assert len(note) == 0
        repo_nota.adaugare(nota_i)
        repo_nota.adaugare(nota_ii)
        note = repo_nota.get_all()
        assert len(note) == 2
        repo_nota.stergere(id_student, nr_lab_prob)
        note = repo_nota.get_all()
        assert len(note) == 1

    def __nume_stud(self):
        id_student = 50
        nume = "Bercea"
        grup = 201
        student = Student(id_student, nume, grup)
        repo_student = RepoStudent()
        students = repo_student.get_all()
        assert len(students) == 0
        repo_student.adaugare(student)
        students = repo_student.get_all()
        assert len(students) == 1
        assert repo_student.nume(50) == "Bercea"

    def __exista_id(self):
        id_student = 50
        nume = "Bercea"
        grup = 201
        student = Student(id_student, nume, grup)
        repo_student = RepoStudent()
        students = repo_student.get_all()
        assert len(students) == 0
        repo_student.adaugare(student)
        students = repo_student.get_all()
        assert len(students) == 1
        assert repo_student.exista_id_student(id_student) == True

    def __exista_nr_lab(self):
        nr_lab_prob = "10_3"
        descriere = "Misto"
        deadline = 30
        problema = Problema(nr_lab_prob, descriere, deadline)
        repo_problema = RepoProblema()
        probleme = repo_problema.get_all()
        assert len(probleme) == 0
        repo_problema.adaugare(problema)
        probleme = repo_problema.get_all()
        assert len(probleme) == 1
        assert repo_problema.exista_nr_lab_prob(nr_lab_prob) == True

    def __medie(self):
        id_student = 1000
        nr_lab_prob = "3_2"
        nota = 7
        nota_i = Note(id_student, nr_lab_prob, nota)
        id_student2 = 1000
        nr_lab_prob2 = "3_3"
        nota2 = 3
        nota_ii = Note(id_student2, nr_lab_prob2, nota2)
        repo_nota = RepoNota()
        note = repo_nota.get_all()
        assert len(note) == 0
        repo_nota.adaugare(nota_i)
        repo_nota.adaugare(nota_ii)
        note = repo_nota.get_all()
        assert len(note) == 2
        assert repo_nota.medie(id_student) == 5

    def __rulare_teste(self):
        self.__adaugare_nota()
        self.__adaugare_problema()
        self.__adaugare_student()
        self.__stergere_problema()
        self.__stergere_student()
        self.__stergere_nota()
        self.__modificare_problema()
        self.__modificare_nota()
        self.__modificare_student()
        self.__adaugare_nota()
        self.__stergere_nota()
        self.__modificare_nota()
        self.__nume_stud()
        self.__exista_id()
        self.__exista_nr_lab()
        self.__medie()

    def run(self):
        print("Se incepe rularea testelor...")
        print("...")
        self.__rulare_teste()
        print("Testele au fost rulate cu succes!\n")