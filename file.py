class File():
    def __init__(self):
        self.file_apprenant = {}
        self.file = open("apprenantmail.txt", "r")

    def get_nom_prenom(self):
        for i in self.file:
            cpt = 0
            while(i[cpt] != "."):
                cpt+=1
            prenom = i[:cpt]
            cpt2 = cpt
            while(i[cpt2] != "@"):
                    cpt2+=1  
            nom = i[cpt+1:cpt2]
            prenom = prenom.title()
            nom = nom.replace("-", " ")
            nom = nom.title()
            self.file_apprenant[nom+" "+prenom] = i
        return(self.file_apprenant)





