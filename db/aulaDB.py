import json

from db.database import Database

class AulaDAO:
    def __init__(self):
        self.db = Database(database='escola', collection='aulas')
        self.collection = self.db.collection

    def create_aula(self, aula):
        print(aula)
        res = self.collection.insert_one({"Aula":aula.assunto,"Professor":aula.professor.to_string(),"Alunos":aula.getListaPresenca()})
        return res.inserted_id
        #
        # data = {"Aula":"aula.assunto","Professor":"aula.professor.to_string()","Alunos":[
        #     {"nome": "Joao", "especialidade": "Matematica"},
        #     {"nome": "Maria", "especialidade": "Portugues"}
        # ]}

        # print(data)
        # self.collection.insert_one(data)

    def read(self, assunto : str):
        return self.collection.find({'Aula': assunto})

    def update(self,assunto_antigo : str, assunto_novo : str):
        return self.collection.update_one(
            {"Aula": assunto_antigo},
            {
                "$set": {"Aula": assunto_novo},
                "$currentDate": {"lastModified": True}
            }
        )

    def delete(self, assunto : str):
        return self.collection.delete_one({"Aula": assunto})