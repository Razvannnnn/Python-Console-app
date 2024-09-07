from domain.student import Student
from domain.problema import Problema
from domain.note import Note
from infrastructura.repo_student import RepoStudent, FileRepoStudenti
from infrastructura.repo_problema import RepoProblema, FileRepoProbleme
from infrastructura.repo_nota import RepoNota, FileRepoNota
from validare.valid_student import ValidStudent
from validare.valid_problema import ValidProblema
from validare.validare_nota import ValidNota
from business.service_student import ServiceStudent
from business.service_problema import ServiceProblema
from business.service_note import ServiceNote
from console import UI
from teste.teste import Teste

valid_student = ValidStudent()
valid_problema = ValidProblema()
valid_nota = ValidNota()
cale_fisier_stud = "infrastructura/studenti.txt"
cale_fisier_prob = "infrastructura/probleme.txt"
cale_fisier_nota = "infrastructura/note.txt"
repo_student = FileRepoStudenti(cale_fisier_stud)
repo_problema = FileRepoProbleme(cale_fisier_prob)
repo_nota = FileRepoNota(cale_fisier_nota)
srv_student = ServiceStudent(repo_student, valid_student)
srv_problema = ServiceProblema(repo_problema, valid_problema)
srv_nota = ServiceNote(repo_problema, repo_student, repo_nota, valid_problema, valid_student, valid_nota)
ui = UI(srv_student, srv_problema, srv_nota)
teste = Teste()
teste.run()
ui.run()

