from domain.clienti import Client

class ValidatorClient:

    def __init__(self, client, lista_clienti):
        self.__client = client
        self.__lista_clienti = lista_clienti
        
    
    '''
     Valideaza id client
     
     id - int > 0, unic
     returneaza: True - id valid, False - id invalid
    '''
    def valideaza_id(self):
        if len(self.__lista_clienti)==0:
            return (int(self.__client.get_id())>0)
        
        else:
            concluzie=True
            for x in self.__lista_clienti:
                if x.get_id()==self.__client.get_id():
                    concluzie=False
            
            return (concluzie and int(self.__client.get_id())>0)
        

    '''
    Verifica daca exista in lista de clienti un client cu cnp-ul dat
    
    returneaza: True - exista cnp, False - nu exista cnp
    '''
    def valideaza_cnp_stergere(self):
        concluzie=False
        for x in self.__lista_clienti:
            if x.get_cnp()==self.__client.get_cnp():
                concluzie=True
        return concluzie
        

    '''
    Valideaza nume client
    
    nume - string, !=""
    returneaza: True - nume valid, False - nume invalid
    '''
    def valideaza_nume(self):
        return (self.__client.get_nume()!="")
    


    '''
    Valideaza cnp client
    
    cnp - lungime 13, unic
    returneaza: True - cnp valid, False - cnp invalid
    '''
    def valideaza_cnp(self):
        concluzie=True
        for x in self.__lista_clienti:
            if x.get_cnp()==self.__client.get_cnp():
                concluzie=False
        
        return (self.__client.get_cnp()!="" and len(self.__client.get_cnp())==13 and concluzie)
    


    '''
    Verifica daca exista cnp-ul in lista
    
    returneaza:True - exista cnp in lista, False - nu exista cnp-ul in lista
    '''
    def valideaza_exista_cnp(self, cnp):
        concluzie=False
        for x in self.__lista_clienti:
            if cnp in x.get_cnp():
                concluzie=True
                break
        return concluzie
        