from domain.filme import Film

class ValidatorFilm:

    def __init__(self, film, lista_filme):
        self.__film = film
        self.__lista_filme = lista_filme
        self.__lista_genuri = ["thriller", "horror", "romance", "distopic", "desen", "comedie", "drama", "politist"]
        

    '''
     Valideaza id film

     id - int > 0, unic
     returneaza: True - id valid, False - id invalid
    '''
    def valideaza_id(self):
        if len(self.__lista_filme)==0:
            return (int(self.__film.get_id())>0)
        
        else:
            concluzie=True
            for x in self.__lista_filme:
                if x.get_id()==self.__film.get_id():
                    concluzie=False
            
            return (concluzie and int(self.__film.get_id())>0)
    

    '''
    Verifica daca id-ul exista
        
    returneaza: True - exista id, False- nu exista id
    '''
    def valideaza_exista_id(self):
        concluzie=False
        for x in self.__lista_filme:
            if x.get_id()==self.__film.get_id():
                concluzie=True
                break
        return concluzie
    

    '''
    Valideaza titlu film
        
    titlu - string, !=""
    returneaza: True - titlu valid, False - titlu invalid
    '''
    def valideaza_titlu(self):
        return (self.__film.get_titlu()!="")
    


    '''
    Valideaza descriere film
        
    descriere - string, !=""
    returneaza: True - descriere valid, False - descriere invalid
    '''
    def valideaza_descriere(self):
        return (self.__film.get_descriere()!="")
    

    '''
    Valideaza gen film
    
    gen - string, !=""
        - apartine listei self.__lista_genuri
    returneaza: True - gen valid, False - gen invalid
    '''
    def valideaza_gen(self):
        return (self.__film.get_gen() in self.__lista_genuri)
        