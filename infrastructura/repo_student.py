from domain.student import Student
from random import *
from utils import Utils

class RepoStudent:
    def __init__(self):
        self._studenti = {

        }

    def adaugare(self, student):
        """
        Adauga un student in lista de studenti
        :param student: obiect
        :return:
        """
        id_student = student.get_id_student()
        if id_student in self._studenti:
            raise Exception("Student existent!")
        self._studenti[id_student] = student

    def modificare(self, student):
        """
        Modifica un student din lista de studenti
        :param student: obiect
        :return:
        """
        id_student = student.get_id_student()
        if id_student not in self._studenti:
            raise Exception("Student inexistent!")
        self._studenti[id_student] = student

    def cautare(self, id_student):
        """
        Cauta un student in lista de studenti si il returneaza
        :param id_student: int unic
        :return: student
        """
        if id_student not in self._studenti:
            raise Exception("Student inexistent!")
        return self._studenti[id_student]

    def stergere(self, id_student):
        """
        Sterge un student din list de studenti
        :param id_student: int unic
        :return:
        """
        if id_student not in self._studenti:
            raise Exception("Student inexistent!")
        del self._studenti[id_student]

    def exista_id_student(self, id_student):
        """
        Verifica daca exista un student in lista de studenti cu id-ul id_student
        :param id_student: int unic
        :return: True sau False
        """
        if id_student not in self._studenti:
            raise Exception("Student inexistent!")
        return True

    '''
    def cmp_nume(self, x, y):
        """
        Functie de comparare a 2 note
        :param x:
        :param y:
        :return: 1 sau 0
        """
        if str(x.get_nume()) == str(y.get_nume()):
            if x.get_nota() < y.get_nota():
                return 1
            else:
                return 0
        if str(x.get_nume()) < str(y.get_nume):
            return 1
        return 0

    def sort_nume(self):
        """
        Sorteaza lista de studenti dupa nume
        :return: lista noua
        """
        values = self._studenti.values()
        values_list = list(values)
        print(values_list)
        studenti_ord = Utils.insertion_sort(values_list, key=lambda x: x, cmp= lambda x,y: self.cmp_nume(x,y))
        #studenti_ord = Utils.comb_sort(values_list, key=lambda x: x.get_nume())
        #studenti_ord = sorted(values_list, key=lambda x: x.get_nume())
        return studenti_ord
    '''


    def nume(self, id_student):
        """
        Returneaza numele unui student cu id-ul id_student
        :param id_student: int unic
        :return: nume
        """
        for student in self._studenti:
            if self._studenti[student].get_id_student() == id_student:
                return self._studenti[student].get_nume()

    def get_all(self):
        """
        Returneaza lista de studenti
        :return: lista studenti
        """
        return self._studenti

    def generate_random_student(self):
        """
        Genereaza un student random si il adauga in lista de studenti
        :return:
        """
        lista_nume = ["Mihai", "Ion", "Bercea", "Maria", "Ilie", "Florin", "Dragos", "Elena", "George", "Miruna",
                      "Dorian", "Alex", "Andrei", "Diana", "Razvan", "Stefan", "Alin"]
        id_student = randrange(1, 9999)
        nume = choice(lista_nume)
        grup = randrange(1, 999)
        student = Student(id_student, nume, grup)
        self.adaugare(student)


class FileRepoStudenti(RepoStudent):
    def __init__(self, cale_fisier):
        RepoStudent.__init__(self)
        self.__cale_fisier = cale_fisier

    def __read_all_studenti_from_file(self):
        with open(self.__cale_fisier,"r") as f:
            self._studenti.clear()
            lines = f.readlines()
            for line in lines:
                if line != "":
                    parts = line.split(",")
                    id_student = int(parts[0])
                    nume = parts[1]
                    grup = int(parts[2])
                    student = Student(id_student, nume, grup)
                    self._studenti[id_student] = student

    def __write_all_studenti_to_file(self):
        with open(self.__cale_fisier,"w") as f:
            for id_student in self._studenti:
                f.write(str(self._studenti[id_student])+"\n")

    def adaugare(self, student):
        self.__read_all_studenti_from_file()
        RepoStudent.adaugare(self, student)
        self.__write_all_studenti_to_file()

    def modificare(self, student):
        self.__read_all_studenti_from_file()
        RepoStudent.modificare(self, student)
        self.__write_all_studenti_to_file()

    def cautare(self, id_student):
        self.__read_all_studenti_from_file()
        return RepoStudent.cautare(self, id_student)

    def stergere(self, id_student):
        self.__read_all_studenti_from_file()
        RepoStudent.stergere(self, id_student)
        self.__write_all_studenti_to_file()

    def exista_id_student(self, id_student):
        self.__read_all_studenti_from_file()
        return RepoStudent.exista_id_student(self, id_student)

    def get_all(self):
        self.__read_all_studenti_from_file()
        return RepoStudent.get_all(self)

    def generate_random_student(self):
        self.__read_all_studenti_from_file()
        RepoStudent.generate_random_student(self)
        self.__write_all_studenti_to_file()

    def nume(self, id_student):
        self.__read_all_studenti_from_file()
        return RepoStudent.nume(self, id_student)
















    def partition(lst, stanga, dreapta):
        # Apelul initial sa fie cu stanga=0 si dreapta = len(lst)-1
        '''
        Returneaza pozitia pivotului (lst[stanga])
        '''
        pivot = lst[stanga]  # pivotul il luam ca fiind cel mai din stanga element
        i = stanga
        j = dreapta
        while i != j:
            while lst[j] >= pivot and i < j:  # Cat timp putem merge cu j-ul in 'stanga'
                j = j - 1
            lst[i] = lst[j]  # toate elementele care sunt mai mici decat pivotul trebuie mutate in stanga pivotului (care e in stanga) i->marginea din stanga
            while lst[i] <= pivot and i < j:  # Cat timp putem merge cu i-ul in 'dreapta'
                i = i + 1
            lst[j] = lst[i]  # toate elementele care sunt mai mari decat pivotul trebuie mutate in stanga pivotului (care e in dreapta) j->marginea din dreapta
        lst[i] = pivot  # punem pivotul pe pozitia pe care ar trebui sa fie
        return i  # returnam pozitia pivotului

    def quick_sort_in_place(lst, stanga, dreapta):
        pos = partition(lst, stanga, dreapta)  # pos este pozitia pivotului in noua lista
        if stanga < pos - 1:  # Daca lista lst[stanga:pos] are elemente
            quick_sort_in_place(lst, stanga, pos - 1)  # Sorteaza lista pana la pozitia pivotului
        if pos + 1 < dreapta:  # Daca lista lst[pos+1:dreapta] are elemente
            quick_sort_in_place(lst, pos + 1, dreapta)  # Sorteaza lista de la pozitia pivotului





def insertion_sort(lst):
    '''
    Se inserează elementul curent pe poziția corectă în subsecvența deja sortată
    În sub-secvența ce conține elementele deja sortate se țin elementele sortate pe tot parcursul algoritmului
    lst->list, lista de elemente
    return->list, lista sortata
    '''
    for i in range(1,len(lst)):
        indice = i-1
        a = lst[i]
        while indice>=0 and a<lst[indice]: # Cat timp mai putem sa mutam la "stanga" elementul de pe pozitia i (lst[i]=a)
            lst[indice+1] = lst[indice]
            indice = indice-1
        lst[indice+1] = a # La final, ultimul element la care s-a ajuns ar trebui sa fie elementul de la care am pornit (adica cel pe care trebuie sa il inseram pe pozitia corecta)
    return lst # Oricum se modifica lista, la alegere daca sa fie returnata sau nu





def binary_search(lst,x,start=0,end=-2):
    '''
    Cautam binar elementul x
    Daca x se afla in lista atunci vom returna pozitia elementului
    lst->list, lista de elemente
    x->orice, elementul cautat
    start->start, start-ul listei
    end->end, sfarsitul listei
    return->int, indicele elementului
    '''
    if end==-2:
        end=len(lst)-1 # Prima oara end ar trebui sa fie lungimea listei
    if start>end:
        return -1
    mijloc=(start+end)//2
    if lst[mijloc]==x:
        return mijloc
    if x>lst[mijloc]:
        return binary_search(lst,x,mijloc+1,end)
    else: return binary_search(lst,x,start,mijloc-1)

def binary_search_nerecursiv(lst,x):
    '''
    Cautam binar elementul x
    Daca x se afla in lista atunci vom returna pozitia elementului
    lst->list, lista de elemente
    x->orice, elementul cautat
    return->int, indicele elementului
    '''
    start=0
    end=len(lst)-1
    while start<=end:
        mijloc=(start+end)//2
        if x==lst[mijloc]:
            return mijloc
        if x>lst[mijloc]:
            start=mijloc+1
        else:end=mijloc-1
    return -1













def merge_sort(lst):
    '''
    Secvența este împărțită în două subsecvențe egale și fiecare subsecvența este sortată
    După sortare se interclasează cele două subsecvențe, astfel rezultă secvența sortată în întregime.
    lst->list, lista de elemente
    return->lst, lista sortata de elemente
    '''
    if len(lst)<=1:
        return lst
    mijloc = len(lst)//2
    stanga=merge_sort(lst[:mijloc])
    dreapta=merge_sort(lst[mijloc:])
    i=0
    j=0
    lista_finala=[]
    while i<len(stanga) and j<len(dreapta):
        if stanga[i]<dreapta[j]:
            lista_finala.append(stanga[i])
            i+=1
        else:
            lista_finala.append(dreapta[j])
            j+=1
    lista_finala+=stanga[i:]
    lista_finala+=dreapta[j:]
    return lista_finala







def selection_sort(lst):
    '''
    Se determină elementul având cea mai mica cheie, interschimbare elementul cu elementul de pe prima pozitie
    -> Apoi se reia procedura pana cand toate elementele sunt sortate
    lst->list, lista data
    return->lst, lista sortata
    '''
    for i in range(0,len(lst)-1):
        indice = i # Va interschimba in final elementul cu indice i, cu cel mai mic element din lista [i+1:]
        # E initializat cu i pentru ca presupunem initial ca lst[i] e pus corect unde e
        for j in range(i+1,len(lst)):
            if (lst[j]<lst[indice]):
                indice =j # Daca gasim un element mai mic decat cel curent schimbam indice
        if (i<indice):
            lst[i],lst[indice]=lst[indice],lst[i] # Interschimbare
    return lst # Oricum s-a modificat lista, la alegere daca sa fie returnat sau nu









def bubble_sort(lst):
    '''
    Compară elemente consecutive, dacă nu sunt în ordinea dorită le interschimbă
    lst->list, lista de elemente
    return->list, lista sortata de numere
    '''
    for j in range(1,len(lst)):
        for i in range(len(lst)-j):
            if lst[i+1]<lst[i]: # Daca elementele de pe pozitii consecutive nu sunt in ordinea corecta
                lst[i], lst[i + 1] = lst[i + 1], lst[i] # Interschimbare
    return lst[:]


def determina_cea_mai_lunga_secventa(lst):
    n = len(lst)
    l = [1] * n  # Pentru orice element exista o secventa care se termina cu el insusi
    p = [-1] * n  # Valoarea de baza care marcheaza sfarsitul secventei

    for i in range(1,n):  # Incepem de la 1 pentru ca pentru elementul 0, deja avem determinat elementele din l si p corect
        for j in range(i):
            if lst[j] <= lst[i] and l[j] + 1 > l[i]:  # daca elementele de pe pozitiile i si j sunt compatibile, si daca lungime este mai mare
                l[i] = l[j] + 1
                p[i] = j

    # Construim vectorul
    max = 0
    indice = 0
    rez = []
    for i in range(n):
        if l[i] > max:
            max = l[i]
            indice = i
    while indice != -1:
        rez.append(lst[indice])
        indice = p[indice]
    rez.reverse()
    return rez
