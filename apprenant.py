import mysql.connector
from script import Script

class Apprenant():
    def __init__(self, apprenant_id_mail, database="binomotron", table="apprenants"):
        self.apprenant_id_mail = apprenant_id_mail
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="root", database=database)
        self.cursor = self.mydb.cursor()
        self.apprenant_id_mail = apprenant_id_mail
        self.table = table


    def give_apprenants_mail(self):
        for id,mail in self.apprenant_id_mail.items():
            self.cursor.execute("""UPDATE %s SET mail = '%s' WHERE id_apprenants = %d""" %(self.table ,mail, id))
        self.mydb.commit()

    def create_table_mail(self):
        self.cursor.execute("""ALTER TABLE apprenants ADD mail""")
        self.mydb.commit()

apprenant_id_mail = Script().id_to_mail() 
Apprenant(apprenant_id_mail).give_apprenants_mail()