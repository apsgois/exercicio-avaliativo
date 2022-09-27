from helper.WriteAJson import writeAJson
from db.aulaDB import AulaDAO
import json

aula = AulaDAO()

class Pessoa(object):
    def __init__(self, nome):
        self.nome = nome

class Professor(Pessoa):
    def __init__(self, especialidade, nome):
        Pessoa.__init__(self, nome)
        self.especialidade = especialidade

    def to_string(self):
        writeAJson(self.__dict__, "professor")
        return {"nome": self.nome, "especialidade": self.especialidade}


class Aluno(Pessoa):
    def __init__(self, matricula: int, curso: str, periodo: int, nome: str):
        super().__init__(nome)
        self.matricula = matricula
        self.curso = curso
        self.periodo = periodo


    def to_string(self):
        writeAJson(self.__dict__, "aluno")
        return [{'matricula': self.matricula, 'curso': self.curso, 'periodo': self.periodo, 'nome': self.nome}]


class Aula:
    def __init__(self, assunto):
        self.professor: Professor = None
        self.alunos: list = []
        self.assunto = assunto


    def getListaPresenca(self) -> str:
        lista = ''
        for aluno in self.alunos:
            lista = lista +  str(aluno.to_string()) + ','
        writeAJson(lista, "lista")
        return lista
def default():
    print('Valor incorreto')


if __name__ == "__main__":
    while True:
        print('''
                      MENU:

                      [1] - Cadastrar nova aula
                      [2] - Ver  aulas cadastradas
                      [3] - Atualizar aulas 
                      [4] - Deletar aulas
                      [5] - Sair
                  ''')
        x = input('Digite a opção desejada: ')
        match x:
            case '1':

                q_alunos = input('Quantos alunos tem na aula? ')
                for q_alunos in range(int(q_alunos)):
                    nome = input('Digite o nome do aluno: ')
                    matricula = input('Digite a matricula do aluno: ')
                    curso = input('Digite o curso do aluno: ')
                    periodo = input('Digite o periodo do aluno: ')
                    aluno = Aluno(matricula, curso, periodo, nome)

                assuntoDaAula = input('Entre com o assunto da aula:')
                p1 = Professor('Banco de dados', 'Renzo')
                Aula1 = Aula(assuntoDaAula)
                Aula1.professor = p1
                Aula1.alunos.append(aluno)
                print(Aula1.getListaPresenca())
                aula.create_aula(Aula1)

            case '2':
                assunto = input('Digite o assunto da aula que deseja ver(Ira aparecer no aula.json):')
                ler = aula.read(assunto)
                writeAJson(ler, 'aula')

            case '3':
                assunto_antigo = input('Digite o assunto da aula que deseja atualizar:')
                assunto_novo = input('Digite o novo assunto da aula:')
                assunto = aula.update(assunto_antigo, assunto_novo)
                # writeAJson(assunto, 'aula')

            case '4':
                assunto = input('Digite o assunto da aula que deseja deletar:')
                aula.delete(assunto)
            case '5':
                break

            case _:
                default()
