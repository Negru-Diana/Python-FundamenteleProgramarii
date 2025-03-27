from domain.clienti import Client
from repository.repoClienti import RepoClient
from validators.validatorClient import ValidatorClient
import string
import random


class ServiceClient:
    def __init__(self, repo_clienti):
        self.__repo_clienti = repo_clienti


    """
    Creeaza un client nou si il adauga in lista de clienti daca datele sunt valide

    id_client - int, > 0
    nume - string nenul
    cnp - string nenul, lungime string = 13

    returneaza: True, daca clientul a fost creat si adaugat cu succes
    eroare: daca unele date sunt invalide
    """
    def adauga_client(self, id_client, nume, cnp):
        client_nou = Client(id_client, nume, cnp)
        validator = ValidatorClient(client_nou, self.__repo_clienti.get_all())
        
        errors = []
        if not validator.valideaza_id():
            errors.append("ID invalid. Trebuie sa fie unic si pozitiv.")
        if not validator.valideaza_nume():
            errors.append("Numele nu poate fi gol.")
        if not validator.valideaza_cnp():
            errors.append("CNP invalid. Trebuie sa aiba 13 cifre si sa fie unic.")
        
        if errors:
            raise ValueError("\n".join(errors))
        self.__repo_clienti.adauga(client_nou)
        return True


    """
    Sterge un client din lista de clienti, daca acesta exista

    id_client - int

    returneaza: True, daca clientul a fost sters cu succes
    eroare: daca clientul cu id-ul dat nu exista in lista de clienti
    """
    def sterge_client(self, id_client):
        clienti = self.__repo_clienti.get_all()
        for client in clienti:
            if client.get_id() == id_client:
                self.__repo_clienti.sterge(client)
                return True
        raise ValueError(f"Clientul cu ID-ul {id_client} nu exista.")


    
    """
    Modifica datele unui client din lista de clienti

    id_vechi - int, > 0 (id-ul vechi al clientului de modificat)
    id_nou - int, > 0 (id-ul nou al clientului de modificat)
    nume_nou - string nenul
    cnp_nou - string nenul, lungime string = 13

    returneaza: True, daca clientul a fost modificat
    eroare: daca datele noi ale clientului sunt invalide
    """
    def modifica_client(self, id_vechi, id_nou, nume_nou, cnp_nou):
        client_vechi = self.cauta_client_dupa_id(id_vechi)
        lista_temp = [c for c in self.__repo_clienti.get_all() if c.get_id() != id_vechi]
        
        client_nou = Client(id_nou, nume_nou, cnp_nou)
        validator = ValidatorClient(client_nou, lista_temp)
        
        errors = []
        if not validator.valideaza_id():
            errors.append("ID invalid. Trebuie sa fie unic si pozitiv.")
        if not validator.valideaza_nume():
            errors.append("Numele nu poate fi gol.")
        if not validator.valideaza_cnp():
            errors.append("CNP invalid. Trebuie sa aiba 13 cifre si sa fie unic.")
        
        if errors:
            raise ValueError("\n".join(errors))
        self.__repo_clienti.modifica(client_nou, client_vechi)
        return True


    """
    Cauta un client dupa id

    id_client - int

    returneaza: Client
    eroare: daca clientul cu id-ul dat nu exista
    """
    def cauta_client_dupa_id(self, id_client):
        for client in self.__repo_clienti.get_all():
            if client.get_id() == id_client:
                return client
        raise ValueError(f"Clientul cu ID-ul {id_client} nu exista.")


    """
    Cauta clienti dupa un string

    search_string - string

    returneaza: lista de clienti care contin acel string in nume
    """
    def cauta_clienti_dupa_string(self, search_string):
        return [client for client in self.__repo_clienti.get_all()
                if search_string.lower() in client.get_nume().lower()]


    """
    Cauta clienti dupa cnp

    cnp - string

    returneaza: Client
    eroare: daca nu exista clientul cu cnp-ul dat
    """
    def cauta_client_dupa_cnp(self, cnp):
        for client in self.__repo_clienti.get_all():
            if client.get_cnp() == cnp:
                return client
        raise ValueError(f"Clientul cu CNP-ul {cnp} nu exista.")


    """
    Returneaza toti clientii din lista de clienti
    """
    def get_all_clienti(self):
        return self.__repo_clienti.get_all()

    """
    Genereaza un client random pe care il adauga la lista de clienti

    returneaza: Client (clientul nou generat)
    """
    def genereaza_client_random(self):
        while True:
            letters= string.ascii_letters
            nume=''.join(random.choice(letters) for i in range(7))
            cnp=""
            for i in range(13):
                cnp=str(cnp)+str(int(random.randint(0,9)))
            
            id_client=int(random.randint(900,14000))
        
            # Verific daca ID-ul exista deja
            try:
                self.cauta_client_dupa_id(id_client)
            except ValueError:
                # Daca nu exista, pot folosi ID-ul generat
                client_nou=Client(id_client,nume,cnp)
                self.__repo_clienti.adauga(client_nou)
                self.__repo_clienti.citeste_din_fisier()
                return client_nou
        
       