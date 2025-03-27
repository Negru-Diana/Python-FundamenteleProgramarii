from domain.clienti import Client

class RepoClient:

    def __init__(self, lista_clienti):
        self.__lista_clienti = lista_clienti


    """
    Adauga un nou client in lista si actualizeaza fisierul

    client_nou - Client
    """
    def adauga(self, client_nou):
        self.__lista_clienti.append(client_nou)
        self.scrie_in_fisier()


    """
    Sterge un client din lista si actualizeaza fisierul

    client_de_sters - Client
    """
    def sterge(self, client_de_sters):
        if client_de_sters in self.__lista_clienti:
            self.__lista_clienti.remove(client_de_sters)
            self.scrie_in_fisier()


    """
    Modifica datele unui client

    client_nou - Client
    client_vechi - Client
    """
    def modifica(self, client_nou, client_vechi):
        if client_vechi in self.__lista_clienti:
            self.__lista_clienti.remove(client_vechi)
            self.__lista_clienti.append(client_nou)
            self.scrie_in_fisier()


    """
    Returneaza lista clientilor
    """
    def get_all(self):
        return self.__lista_clienti



    """
    Scrie clientii din lista in fisier
    """
    def scrie_in_fisier(self):
        f=open("clienti.txt","w")
        for x in self.__lista_clienti:
            f.write(str(x.get_id())+";"+str(x.get_nume())+";"+str(x.get_cnp())+"\n")
        f.close()


    """
    Incarca clientii din fisier
    """
    def citeste_din_fisier(self):
        self.__lista_clienti=[]
        f=open("clienti.txt","r")
        for x in f:
            if ";" not in x:
                continue
            text=x.split(";")
            client_nou=Client(text[0],text[1],text[2].strip())
            self.__lista_clienti.append(client_nou)
        f.close()