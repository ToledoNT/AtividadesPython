
class Alunos:
    def __init__(self, doc, nome, matricula, curso):
        self.doc = doc
        self.nome = nome
        self.matricula = matricula
        self.curso = curso 
class Curso:
    def __init__(self, nome, periodo):
        self.nome = nome 
        self.periodo = periodo
        
class Professor:
    def __init__(self, nome , disciplina, numero, curso ):
        self.nome = nome
        self.disciplina = disciplina
        self.numero = numero 
        self.curso = curso 
        