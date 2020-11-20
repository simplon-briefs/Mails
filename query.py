import mysql.connector
class Query():
    def __init__(self):
        self.query_apprenants = {}
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="binomotron")
        self.cursor = self.mydb.cursor()

    def get_apprenants(self):
        self.cursor.execute("""SELECT * FROM apprenants""")
        for i in self.cursor.fetchall():
            nom = i[1]
            nom = nom.replace("'", "")
            prenom = i[2]
            self.query_apprenants[nom+" "+prenom] = i[0]
        return(self.query_apprenants)





