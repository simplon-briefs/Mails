from file import File
from query import Query

class Script():
    def __init__(self):
        self.file_apprenants = File().get_nom_prenom()
        self.query_apprenants = Query().get_apprenants()
        self.retour = {}

    def id_to_mail(self):
        for i in self.file_apprenants:
            self.retour[self.query_apprenants[i]] = self.file_apprenants[i]
        return(self.retour)