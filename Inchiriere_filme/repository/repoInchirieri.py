from domain.inchirieri import Inchiriere

class RepoInchiriere:

    def __init__(self, lista_inchirieri):
        self.__lista_inchirieri = lista_inchirieri


    """
    Adauga o noua inchiriere in lista si actualizeaza fisierul

    inchiriere_noua - Inchiriere
    """
    def adauga(self, inchiriere_noua):
        self.__lista_inchirieri.append(inchiriere_noua)
        self.scrie_in_fisier()


    """
    Sterge o inchiriere din lista si actualizeaza fisierul

    inchiriere_de_sters - Inchiriere
    """
    def sterge(self, inchiriere_de_sters):
        if inchiriere_de_sters in self.__lista_inchirieri:
            self.__lista_inchirieri.remove(inchiriere_de_sters)
            self.scrie_in_fisier()


    """
    Modifica datele unei inchirieri

    inchiriere_noua - Inchiriere
    inchiriere_veche - Inchiriere
    """
    def modifica(self, inchiriere_noua, inchiriere_veche):
        if inchiriere_veche in self.__lista_inchirieri:
            self.__lista_inchirieri.remove(inchiriere_veche)
            self.__lista_inchirieri.append(inchiriere_noua)
            self.scrie_in_fisier()


    """
    Returneaza lista inchirierilor
    """
    def get_all(self):
        return self.__lista_inchirieri


    """
    Scrie filmele din lista in fisier
    """
    def scrie_in_fisier(self):
        f=open("inchirieri.txt","w")
        for x in self.__lista_inchirieri:
            f.write(str(x.get_id() +";"+x.get_id_film()+";"+x.get_cnp_client()+";"+x.get_data_inchiriere()+";"+x.get_data_retur()+"\n"))
        f.close()


    """
    Incarca filmele din fisier
    """
    def citeste_filme_din_fisier(self):
        self.__lista_filme=[]
        f=open("inchirieri.txt","r")
        for x in f:
            if ";" not in x:
                continue
            text=x.split(";")
            inchiriere_noua=Inchiriere(text[0],text[1],text[2],text[3],text[4].strip())
            self.__lista_inchirieri.append(inchiriere_noua)
        f.close()