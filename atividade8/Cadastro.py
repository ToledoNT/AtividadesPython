from classe import Alunos, Curso, Professor

ads = Curso("Analise e Dev de Sistemas", "Noturno")
biomed = Curso("Biomedicina", "Integral")
medicina = Curso("Medicina", "Integral")


aluno_lucas = Alunos("231321", "Lucas", "01", ads)
aluno_vanley = Alunos("21321", "Vanley", "02", biomed)
aluno_alisson = Alunos("72836782163","Alisson" , "03", medicina)

profiuri = Professor("Iuri", "Programação", "01", ads)
profromario = Professor("Romario","Laboratorio informatica", "032", biomed)
profdunga = Professor ("Dunga", "Anatomia Humana", "03", medicina)

print(aluno_lucas.curso.periodo)
print(aluno_vanley.curso.nome)
print(aluno_alisson.curso.nome)
