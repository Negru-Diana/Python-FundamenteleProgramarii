from domain.inchirieri import Inchiriere

class ValidatorInchiriere:

    def __init__(self, inchiriere, lista_inchirieri):
        self.__inchiriere = inchiriere
        self.__lista_inchirieri = lista_inchirieri
        

    '''
    Valideaza id inchiriere
        
    id - int > 0, unic
        
    returneaza: True - id valid, False - id invalid
    '''
    def valideaza_id_inchiriere(self):
       
        if len(self.__lista_inchirieri)==0:
            return (int(self.__inchiriere.get_id())>0)
        
        else:
            concluzie=True
            for x in self.__lista_inchirieri:
                if x.get_id()==self.__inchiriere.get_id():
                    concluzie=False
            
            return (concluzie and int(self.__inchiriere.get_id())>0)